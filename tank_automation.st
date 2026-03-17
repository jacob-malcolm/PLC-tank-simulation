PROGRAM PLC_PRG
VAR
	test_counter : INT := 0;
	cycle_time : REAL := 0.1;
	target_level : REAL := 50.0;     // Desired tank level
    Kp : REAL := 1.2;                // Proportional gain
    Ki : REAL := 0.5;                // Integral gain
    Kd : REAL := 0.1;                // Derivative gain
    error : REAL;
    integral : REAL := 0;
    derivative : REAL;
    last_error : REAL := 0;
    valve_output : REAL;
END_VAR


test_counter := test_counter + 1;
// Simple tank filling physics

// --- PID CALCULATION ---
error := target_level - GVL_Tank.tank_level;
integral := integral + error * cycle_time;
derivative := (error - last_error) / cycle_time;

valve_output := Kp*error + Ki*integral + Kd*derivative;

// Clamp valve_output to 0–5 (your previous max flow)
IF valve_output > 5.0 THEN
    valve_output := 5.0;
ELSIF valve_output < 0.0 THEN
    valve_output := 0.0;
END_IF

last_error := error;

// --- TANK PHYSICS ---
GVL_Tank.flow_in := valve_output;

GVL_Tank.tank_level :=
    GVL_Tank.tank_level +
    (GVL_Tank.flow_in - GVL_Tank.flow_out) * cycle_time;

// Clamp tank level
IF GVL_Tank.tank_level > 100.0 THEN
    GVL_Tank.tank_level := 100.0;
END_IF;

IF GVL_Tank.tank_level < 0.0 THEN
    GVL_Tank.tank_level := 0.0;
END_IF;

// --- ALARM CONDITION ---
IF GVL_Tank.tank_level >= 95.0 THEN
    GVL_Tank.alarm_state := TRUE;
ELSE
    GVL_Tank.alarm_state := FALSE;
END_IF;

// --- FILL TIMER ---
IF valve_output > 0 THEN
    GVL_Tank.fill_time := GVL_Tank.fill_time + cycle_time;
ELSE
    GVL_Tank.fill_time := 0.0;
END_IF;
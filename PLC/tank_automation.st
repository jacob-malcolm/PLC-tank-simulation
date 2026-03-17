PROGRAM PLC_PRG
VAR
	test_counter : INT := 0;
	cycle_time : REAL := 0.1;
END_VAR


test_counter := test_counter + 1;
// Simple tank filling physics

// Determine inflow
IF GVL_Tank.valve_state THEN
    GVL_Tank.flow_in := 5.0;
ELSE
    GVL_Tank.flow_in := 0.0;
END_IF;


// Tank physics
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


// Valve control
IF GVL_Tank.tank_level < 30.0 THEN
    GVL_Tank.valve_state := TRUE;
END_IF;

IF GVL_Tank.tank_level >= 80.0 THEN
    GVL_Tank.valve_state := FALSE;
END_IF;


// Alarm condition
IF GVL_Tank.tank_level >= 95.0 THEN
    GVL_Tank.alarm_state := TRUE;
END_IF;


// Fill timer
IF GVL_Tank.valve_state THEN
    GVL_Tank.fill_time := GVL_Tank.fill_time + cycle_time;
ELSE
    GVL_Tank.fill_time := 0.0;
END_IF;
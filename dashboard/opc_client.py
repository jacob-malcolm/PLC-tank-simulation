from opcua import Client
import random

url = "opc.tcp://localhost:4840"

demo_mode = False

try:
    client = Client(url)
    client.set_user(None)
    client.connect()

    tank = client.get_node('ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_Tank.tank_level')
    valve = client.get_node('ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_Tank.valve_state')
    alarm = client.get_node('ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_Tank.alarm_state')

except:
    demo_mode = True


def read_values():

    if demo_mode:
        tank_level = random.uniform(20, 80)
        valve_state = random.choice([True, False])
        alarm_state = False
    else:
        tank_level = tank.get_value()
        valve_state = valve.get_value()
        alarm_state = alarm.get_value()

    return tank_level, valve_state, alarm_state

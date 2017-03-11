from ev3dev.ev3 import *
from time import sleep

m=LargeMotor('outB')
n=LargeMotor('outC')
btn = Button()
i = 0
while(i < 1):
    if btn.any():
        m.run_to_rel_pos(position_sp=775, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=775, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=180, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=-160, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=1100, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=1000, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=180, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=-160, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=700, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=700, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=180, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=-160, speed_sp=500, stop_action="hold")
        sleep(2)
        m.run_to_rel_pos(position_sp=1100, speed_sp=500, stop_action="hold")
        n.run_to_rel_pos(position_sp=1100, speed_sp=500, stop_action="hold")
        i = 1
    else:
        sleep(0.01)

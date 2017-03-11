from ev3dev.ev3 import *
from time import sleep

m=LargeMotor('outB')
n=LargeMotor('outC')
m.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
n.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")


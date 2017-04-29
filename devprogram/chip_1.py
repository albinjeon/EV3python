from ev3dev.ev3 import *
from time import sleep

us = UltrasonicSensor() 
us.mode='US-DIST-CM'
units = us.units
distance = us.value()/10
m=LargeMotor('outB')
n=LargeMotor('outC') 
o=MediumMotor('outA')
def gostr(r):
    i = 0
    while(i<r):
        n.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action="hold")
        sleep(1)
        m.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action="hold")
        sleep(1)
        i+=1
def turn_l(d):
    i=0   # 6.5 = 180 degrees
    while(i<d):
        n.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action="hold")
        sleep(1)
        i+=0.5
        m.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action="hold")
        sleep(1)
        i+=0.5
def turn_r(d):
    i=0
    while(i<d):
        n.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action="hold")
        sleep(1)
        i+=0.5
        m.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action="hold")
        sleep(1)
        i+=0.5
def son_rct():
    o.run_timed(time_sp=4000, speed_sp=-75)
    sleep(5)
    o.run_to_rel_pos(position_sp=100, speed_sp=150)
son_rct()
while True:
    distance = us.value()/10
    if(distance < 20):
        turn_l(2)
    else:
        gostr(1)

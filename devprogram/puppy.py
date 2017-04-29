from ev3dev.ev3 import *
from time import sleep
import random
import time

m=LargeMotor('outA')
n=LargeMotor('outD')
btn = Button()

class timerClass(object):
    def __init__(self):
        self._st     = time.clock()


    def getTime(self):
        return time.clock() - self._st

    def reset(self):
        self._st = time.clock()

timer_1 = timerClass()
timer_2 = timerClass()
timer_3 = timerClass()

def DN():
    m.run_timed(time_sp=1000, speed_sp=100)
    n.run_timed(time_sp=1000, speed_sp=100)

def UP():
    m.run_to_rel_pos(position_sp=-70, speed_sp=60, stop_action="brake")
    n.run_to_rel_pos(position_sp=-70, speed_sp=60, stop_action="brake")

def RST():
	P_T = random.randrange(3,7)#3이상 7미만
	F_T = random.randrange(2,5)#2이상 4이하
	P_C = 1
	F_C = 1
	timer_1.reset()
	timer_2.reset()
	timer_3.reset()
	CS(0)

def CS(i):
	if(DB_S != i):
	    DB_S = i
	    NS = True 

def MON():
	if(timer_2.getTime() > 10):
		timer_2.reset()
		P_C -= 1
		if(P_C < 0):
			P_C = 0
	if(timer_1.getTime() > 20):
		timer_1.reset()
		F_C -= 1
		if(F_C < 0):
			F_C = 0
	if(timer_3.getTime() > 30):
		timer_3.reset()
		cs(1)

DN()
sleep(1)
UP()
RST()
while True:
    MON()
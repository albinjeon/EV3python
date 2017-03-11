from time import sleep
from random import choice, randint
import ev3dev.ev3 as ev3

ev3.LargeMotor('outB').run_timed(time_sp=1000, speed_sp=500)
ev3.LargeMotor('outC').run_timed(time_sp=1000, speed_sp=-500)
sleep(2)

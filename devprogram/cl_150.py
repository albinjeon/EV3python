from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode='COL-AMBIENT'

while True:
    print(cl.value())
    sleep(0.5)
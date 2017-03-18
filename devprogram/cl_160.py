from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode='COL-AMBIENT'
clc = 0

while True:
    print(cl.value())
    if (clc + 10 < cl.value() or clc - 10 >cl.value()):
        Sound.beep()
        clc = cl.value()
    else:
        clc = cl.value()
    sleep(0.5)
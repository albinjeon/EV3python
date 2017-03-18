from ev3dev.ev3 import *
from time   import sleep

cl = ColorSensor() 
cl.mode='RGB-RAW'

while True:
    red = cl.value(0)
    green=cl.value(1)
    blue=cl.value(2)
    print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
    sleep(0.5)
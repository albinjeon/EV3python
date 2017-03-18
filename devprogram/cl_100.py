from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')
while True:
    print(colors[cl.value()])
    sleep(0.5)
    Sound.beep()
from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')
clc = 'unknown'
while True:
    print(colors[cl.value()])
    if(clc != colors[cl.value()]):
        Sound.beep()
        clc = colors[cl.value()]
    sleep(0.5)
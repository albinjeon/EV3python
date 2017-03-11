from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
width = 178
height = 128
lcd.draw.text((width/2-35,height/2),'Hello, world.', fill='black')
lcd.update()
sleep(6)
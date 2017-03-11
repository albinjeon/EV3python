from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.text((0,0),'Hello, world.', fill='black')
lcd.update()
sleep(6)
from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.line((0,60), fill='black', width=120)
lcd.update()
sleep(6)
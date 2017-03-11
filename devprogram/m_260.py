from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.rectangle((59,34,119,94), fill='black')
lcd.update()
sleep(6)
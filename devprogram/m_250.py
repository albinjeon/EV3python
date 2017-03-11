from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.rectangle((10,10,60,110), fill='black')
lcd.update()
sleep(6)
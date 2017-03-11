from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
def drawown(r,mx,my):
    lcd.draw.ellipse((mx-r,my-r,mx+r,my+r))
    lcd.update()
    sleep(6)
drawown(30,89,64)
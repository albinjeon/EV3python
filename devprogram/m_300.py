from ev3dev.ev3 import *
from time import sleep
import random

lcd = Screen()
width = 178
height = 128
i=0
btn = Button()
def drawown(r,mx,my):
    lcd.draw.ellipse((mx-r,my-r,mx+r,my+r))
    lcd.update()
    sleep(0.3)
while(i<=0):
    if btn.any():
        i+=1
    else:
        drawown(random.randrange(10,60),random.randrange(0,width),random.randrange(0,height))
    
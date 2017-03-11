from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
def drawrec(n,mx,my):
    lcd.draw.rectangle((mx-(n/2),my-(n/2),mx+(n/2),my+(n/2)), fill='black')
    lcd.update()
    sleep(6)
drawrec(60,89,64)
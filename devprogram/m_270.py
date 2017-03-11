from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
def drawrec(n):
    lcd.draw.rectangle(((178-n)/2,(128-n)/2,(178-n)/2+n,(128-n)/2+n), fill='black')
    lcd.update()
    sleep(6)
drawrec(60)
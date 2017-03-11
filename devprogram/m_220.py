from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
y = 0
line =1
height = 128
while(y<height):
    lcd.draw.text((0,y),'Hello, world #'+str(line),fill='black')
    y += 10
    line+= 1
lcd.update() 
sleep(6)
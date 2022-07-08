from machine import ADC, Pin ,PWM
from utime import sleep
servoPIN = PWM(Pin(16))
servoPIN.freq(50)
ldr = ADC(Pin(27))

def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPIN.duty_u16(int(newDuty))

while True:
     if ldr.read_u16() > 800:#修改數值，介於暗電阻～亮電阻之間
         servo(69)
         sleep(0.2)
         servo(0)
     sleep(3)
     
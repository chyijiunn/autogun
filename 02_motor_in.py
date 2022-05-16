from machine import ADC, Pin ,PWM
from utime import sleep
servoPIN = PWM(Pin(16))
servoPIN.freq(50)

def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPIN.duty_u16(int(newDuty))

servo(180)
sleep(1)
servo(120)
sleep(0.3)
servo(180)

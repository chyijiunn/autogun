from machine import ADC, Pin ,PWM
from utime import sleep
servotrigger = PWM(Pin(16))
servotrigger.freq(50)
servoload = PWM(Pin(26)) 
servoload.freq(50)

def servotri(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servotrigger.duty_u16(int(newDuty))

servoload.duty_u16(6110)
sleep(2)
servoload.duty_u16(5000)
sleep(1)
servoload.duty_u16(4200)
servoload.deinit()
'''
sleep(10)
servotri(180)
sleep(0.5)
servotri(120)
sleep(0.3)
servotri(180)
'''
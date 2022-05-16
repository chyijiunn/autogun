from machine import ADC, Pin ,PWM
from sys import exit
from utime import sleep

LED_b = Pin(25,Pin.OUT)
LED = Pin(17,Pin.OUT)
ldr = ADC(Pin(27))

servoPIN = PWM(Pin(16))
servoPIN.freq(50)

LED.value(1)
LED_b.value(0)
def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPIN.duty_u16(int(newDuty))

while True:
    sleep(1)
    if ldr.read_u16() > 1000:
        sleep(1)
        servo(69)
        sleep(0.3)
        servo(0)
        LED.value(0)
        LED_b.value(1)
        print(ldr.read_u16())
        exit()
    
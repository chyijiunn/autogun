from machine import Pin, PWM,ADC
from time import sleep
servo_pull = PWM(Pin(26))     # PWM pin for servoPull
servo_triger = PWM(Pin(16))  # PWM pin for servoTrigger
ldr = ADC(Pin(27))
servo_pull.freq(50)
servo_triger.freq(50)

def pull():
    servo_pull.duty_u16(2000)
    sleep(0.5)
    for i in range(50):
        servo_pull.duty_u16(160*i+1000)
        sleep(0.1)
    servo_pull.duty_u16(2000)   
    sleep(1)
    servo_pull.deinit()
    
def trigger():
    def servo(degrees):
        if degrees > 180: degrees=180
        if degrees < 0: degrees=0
        maxDuty=9000
        minDuty=1000
        newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
        servo_triger.duty_u16(int(newDuty))
    servo(180)
    sleep(1)
    servo(120)
    sleep(0.3)
    servo(180)

for i in range(3):
    pull()
    while True:
     if ldr.read_u16() > 900:
         trigger()
         break
    
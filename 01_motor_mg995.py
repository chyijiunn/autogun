from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(26))     # the Pico PWM pin
servo.freq(50)
print(servo.duty_u16())

servo.duty_u16(1000)   
sleep(0.5)
for i in range(200):
    servo.duty_u16(40*i+1000)
    sleep(0.1)
servo.duty_u16(2000)   
sleep(1)
servo.deinit()               

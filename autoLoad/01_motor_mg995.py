from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(26))     # the Pico PWM pin
servo.freq(50)
servo.duty_u16(2000)
sleep(0.5)
for i in range(50):
    servo.duty_u16(160*i+1000)
    sleep(0.1)
servo.duty_u16(2000)   
sleep(1)
servo.deinit()               

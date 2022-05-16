from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(26))     # the Pico PWM pin
servo.freq(50)

servo.duty_u16(6110)
sleep(3)
servo.duty_u16(5000)
sleep(1)
servo.duty_u16(4700)
sleep(5)
servo.deinit()
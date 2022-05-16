from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(26))     # the Pico PWM pin
servo.freq(50)
print(servo.duty_u16())
'''
servo.duty_u16(7000)   
sleep(0.75)
servo.duty_u16(5000)   
sleep(1)
servo.duty_u16(4500)  
sleep(0.1)      
servo.deinit()               
'''
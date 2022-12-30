from machine import Pin, PWM,ADC
from time import sleep
ldr = ADC(Pin(27))

while True:
    print(ldr.read_u16())
    sleep(0.5)
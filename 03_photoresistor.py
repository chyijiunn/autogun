# https://www.freva.com/ldr-light-sensor-on-raspberry-pi-pico
from machine import ADC, Pin
from time import sleep
LED = Pin(17,Pin.OUT)
ldr = ADC(Pin(27))#光敏接類比腳位 GP27，可更動 GP 26 ~ 28
LED.value(0)
LED.value(1)
while True:
     print(ldr.read_u16())
     sleep(1)

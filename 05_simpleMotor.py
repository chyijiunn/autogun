#此程式捨棄函式，僅簡單呈現
from machine import ADC, Pin ,PWM
from utime import sleep
LED = Pin(17,Pin.OUT)#定義LED腳位
ldr = ADC(Pin(27))#定義光敏電阻腳位
servoPIN = PWM(Pin(16))#定義馬達橘色線
servoPIN.freq(50)

while True:
     if ldr.read_u16() > 800: #修改數值，介於暗電阻～亮電阻之間
         servoPIN.duty_u16(4000)    # x = 1000 ~ 9000，為擊發數值
         sleep(0.3)#停頓0.3秒
         servoPIN.duty_u16(5000)    # x = 1000 ~ 9000，為歸零數值

         
         
     
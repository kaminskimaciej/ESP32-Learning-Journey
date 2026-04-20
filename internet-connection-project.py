import network
import time
from machine import Pin, I2C
import ssd1306

WIFI_SSID = 'xxxx'
WIFI_PASSWORD = 'xxxx'

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def connect_wifi():
    time.sleep(2)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    oled.fill(0)
    
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        timeout = 10
        dots = ""
        
        while not wlan.isconnected() and timeout > 0:
                    oled.fill(0)
                    oled.text("Connecting" + dots, 0, 0)
                    oled.show()
                    
                    dots = dots + "."
                    if len(dots) > 3:
                        dots = ""
                        
                    time.sleep(1)
                    timeout -= 1
        
        if wlan.isconnected():
            oled.fill(0)
            oled.text("Connected!", 0, 0)
            oled.text(str(wlan.ifconfig()[0]), 0, 20)
            oled.show()
        else:
            oled.fill(0)
            oled.text("Con Failed",0 ,0)
            oled.show()
            
   
connect_wifi()

while True:
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("Everything is ok")
    else:
        print("Connection error")
            
    time.sleep(10)
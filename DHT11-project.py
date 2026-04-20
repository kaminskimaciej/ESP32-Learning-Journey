from machine import Pin, I2C
import time
import dht
import ssd1306

#sensor init
sensor = dht.DHT11(Pin(5))

#screen init
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#getting data from dht11 sensor
def call_dht():
    try:
        sensor.measure()
        return sensor.temperature(), sensor.humidity()
    except OSError as e:
        print('Sensor error')
        return None, None
#printing out data from sensor to OLED screen
def screen_call():
    temp, hum = call_dht()
    oled.fill(0)
    
    if temp is not None and hum is not None:
        oled.fill(0)
        oled.text("Temp: " + str(temp) + "C", 0, 0)
        oled.text("Hum: " + str(hum) + "%", 0, 20)
    else:
        oled.text("Data error", 0 ,0)
            
    oled.show()

while True:
    screen_call()
    
    time.sleep(2)
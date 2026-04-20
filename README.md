# ESP32 Learning Journey

Welcome to my repository! This is my personal workspace where I document my progress in mastering **ESP32** microcontrollers and **MicroPython**.

## Projects
### 01. DHT11 Sensor & OLED Display
A beginner-friendly weather monitoring project.
- **Goal:** Read environmental data (temperature and humidity) and display it in real-time.
- **Hardware used:** - ESP32 Development Board
  - DHT11 Temperature & Humidity Sensor
  - 0.96" I2C OLED Display (128x64)

## Wiring Table

| Component | ESP32 GPIO |
| :--- | :--- |
| DHT11 DATA | GPIO 5 |
| OLED SDA | GPIO 21 |
| OLED SCL | GPIO 22 |

## How to run
1. Ensure you have the `ssd1306.py` library uploaded to your ESP32.
2. Upload the `DHT11-project.py` file to your board.
3. Run the script and observe the data on the OLED display.

### 02. WiFi Connection
Learning how to connect the ESP32 to a local network using MicroPython.
- **Goal:** Enable internet connectivity and obtain an IP address.
- **Features:** - Dynamic connection status display on the OLED screen.
  - Visual loading animation ("Connecting...").
  - Automated network status verification in the main loop.

## Setup
1. Update `WIFI_SSID` and `WIFI_PASSWORD` in the script.
2. Ensure `ssd1306.py` is available on the device.
3. Run the script and check the OLED display for the assigned local IP address.
---
*Created by Maciej Kaminski*

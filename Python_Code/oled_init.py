from machine import Pin, I2C
import ssd1306

# Initialize I2C for the OLED display on alternative pins
i2c = I2C(1, scl=Pin(3), sda=Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def display_message(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

display_message("Hello, World!")

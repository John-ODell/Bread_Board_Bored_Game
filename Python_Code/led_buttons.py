from machine import Pin
import time

# Initialize the LEDs and buttons
led_red = Pin(17, Pin.OUT)
led_blue = Pin(18, Pin.OUT)
button_red = Pin(19, Pin.IN, Pin.PULL_UP)
button_blue = Pin(20, Pin.IN, Pin.PULL_UP)

led_red.off()
led_blue.off()

while True:
    if button_red.value() == 0:
        led_red.on()
        print("Red button pressed!")
    else:
        led_red.off()

    if button_blue.value() == 0:
        led_blue.on()
        print("Blue button pressed!")
    else:
        led_blue.off()

    time.sleep(.15)

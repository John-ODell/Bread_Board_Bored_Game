from machine import Pin
import time

# Initialize the rotary encoder
clk = Pin(14, Pin.IN, Pin.PULL_UP)
dt = Pin(15, Pin.IN, Pin.PULL_UP)
sw = Pin(16, Pin.IN, Pin.PULL_UP)

# Variables to track the rotary encoder position
last_clk = clk.value()
position = 0

while True:
    current_clk = clk.value()
    current_dt = dt.value()

    if current_clk != last_clk:
        if current_dt != current_clk:
            position += 1
        else:
            position -= 1
        print("Position:", position)
        last_clk = current_clk


    if not sw.value():
        print("Button pressed!")

        position = 0

    time.sleep(0.01)

from machine import ADC, Pin
import time

# Initialize the joystick axes on GP26 and GP27
x_axis = ADC(Pin(26))
y_axis = ADC(Pin(27))

# Define a small variance 
variance = 0.05

prev_x = x_axis.read_u16() * (3.3 / 65535)
prev_y = y_axis.read_u16() * (3.3 / 65535)

movement_registered = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

def get_voltage(adc):
    return adc.read_u16() * (3.3 / 65535)

while True:
    x_value = get_voltage(x_axis)
    y_value = get_voltage(y_axis)

    if x_value > prev_x + variance and not movement_registered["up"]:
        print("Joystick moved up!")
        movement_registered["up"] = True
    elif x_value < prev_x - variance and not movement_registered["down"]:
        print("Joystick moved down!")
        movement_registered["down"] = True

    if y_value > prev_y + variance and not movement_registered["right"]:
        print("Joystick moved right!")
        movement_registered["right"] = True
    elif y_value < prev_y - variance and not movement_registered["left"]:
        print("Joystick moved left!")
        movement_registered["left"] = True

    if abs(x_value - prev_x) < variance and abs(y_value - prev_y) < variance:
        movement_registered = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        
    prev_x = x_value
    prev_y = y_value

    print("X-axis:", x_value, "Y-axis:", y_value)

    time.sleep(0.1)

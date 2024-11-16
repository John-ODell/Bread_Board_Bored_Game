from machine import Pin, ADC, I2C
import ssd1306
import time
import random

# Initialize the rotary encoder
clk = Pin(14, Pin.IN, Pin.PULL_UP)
dt = Pin(15, Pin.IN, Pin.PULL_UP)
sw = Pin(16, Pin.IN, Pin.PULL_UP)

# Initialize the LEDs and buttons
led_red = Pin(17, Pin.OUT)
led_blue = Pin(18, Pin.OUT)
button_red = Pin(19, Pin.IN, Pin.PULL_UP)
button_blue = Pin(20, Pin.IN, Pin.PULL_UP)

# Initialize the joystick axes on GP26 and GP27
x_axis = ADC(Pin(26))
y_axis = ADC(Pin(27))

# Initialize I2C for the OLED display on alternative pins
i2c = I2C(1, scl=Pin(3), sda=Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

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

last_clk = clk.value()
position = 0
rotary_sum = 0

def display_message(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

def get_voltage(adc):
    return adc.read_u16() * (3.3 / 65535)

def check_joystick():
    global prev_x, prev_y
    x_value = get_voltage(x_axis)
    y_value = get_voltage(y_axis)
    direction = None

    if x_value > prev_x + variance and not movement_registered["up"]:
        direction = "up"
        movement_registered["up"] = True
    elif x_value < prev_x - variance and not movement_registered["down"]:
        direction = "down"
        movement_registered["down"] = True
    elif y_value > prev_y + variance and not movement_registered["right"]:
        direction = "right"
        movement_registered["right"] = True
    elif y_value < prev_y - variance and not movement_registered["left"]:
        direction = "left"
        movement_registered["left"] = True

    if abs(x_value - prev_x) < variance and abs(y_value - prev_y) < variance:
        movement_registered["up"] = False
        movement_registered["down"] = False
        movement_registered["left"] = False
        movement_registered["right"] = False

    prev_x = x_value
    prev_y = y_value

    print(f"Joystick X: {x_value}, Y: {y_value}, Direction: {direction}")  # Debugging statement
    return direction


def check_rotary():
    global last_clk, position, rotary_sum
    current_clk = clk.value()
    current_dt = dt.value()

    if current_clk != last_clk:
        if current_dt != current_clk:
            position += 1
        else:
            position -= 1
            if position < 0:
                position = 0  # Prevent negative position
        last_clk = current_clk

    if not sw.value():
        position = 0

    rotary_sum += position
    print(f"Rotary sum: {rotary_sum}, Position: {position}, CLK: {current_clk}, DT: {current_dt}")  # Debugging statement
    return rotary_sum

def check_buttons():
    red_button_state = button_red.value()
    blue_button_state = button_blue.value()

    print(f"Red button state: {red_button_state}, Blue button state: {blue_button_state}")  # Debugging statement

    if red_button_state == 0:
        return "red"
    elif blue_button_state == 0:
        return "blue"
    return None

# Main game loop
level = 1
sequence = []

while True:
    for _ in range(level):
        device = random.choice(["rotary", "joystick", "led"])
        if device == "rotary":
            sequence.append(("rotary", random.randint(1, 10)))
        elif device == "joystick":
            sequence.append(("joystick", random.choice(["up", "down", "left", "right"])))
        elif device == "led":
            sequence.append(("led", random.choice(["red", "blue"])))

    for device, value in sequence:
        if device == "rotary":
            display_message(f"Rotary: {value}")
        elif device == "joystick":
            display_message(f"Joystick: {value}")
        elif device == "led":
            display_message(f"LED: {value}")
        time.sleep(5)
        display_message("")

    display_message("Input")

    for device, value in sequence:
        user_input = None
        while user_input is None:
            if device == "rotary":
                user_input = check_rotary()
                print(f"Rotary input: {user_input}")  # Debugging statement
                if user_input != value:
                    display_message("Game Over!")
                    time.sleep(2)
                    level = 1
                    sequence = []
                    #rotary_sum = 0  # Reset rotary sum
                    break
            elif device == "joystick":
                user_input = check_joystick()
                print(f"Joystick input: {user_input}")  # Debugging statement
                if value == "left" and user_input == "left":
                    while user_input != "right":
                        user_input = check_joystick()
                elif value == "up" and user_input:
                    while user_input != "down":
                        user_input = check_joystick()
                if user_input != value:
                    display_message("Game Over!")
                    time.sleep(2)
                    level = 1
                    sequence = []
                    break
            elif device == "led":
                user_input = check_buttons()
                print(f"Button input: {user_input}")  # Debugging statement
                if user_input != value:
                    display_message("Game Over!")
                    time.sleep(2)
                    level = 1
                    sequence = []
                    break

    
    if user_input == value:
        level += 1
        display_message(f"Level {level}")
        time.sleep(2)

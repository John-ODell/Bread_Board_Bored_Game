Bread Board Game - John O'Dell (johncodell@outlook.com)

This is an early alpha build game for a bread board and micropython.
It works for most board but the example is using Pi Pico 2
Change the pinouts as needed.

Items needed
- Any Micropython Compatable Microcontroller
- Joystick Module
- Rotary Dial Module
- 2 Button Module
- 2 LED of different colors (not required but adds to it)
    - 220 Resistors
- .96 OLED screen
- Jumper Wire
- Breadboard

EXAMPLES AND TESTING

.96 OLED Screen example
Pin Outs 
    - .96 OLED screen pins
    - SCL/SCK -> GPIO 3
    - SDA -> GPIO 2
    - VCC -> 3.3v
    - GND -> GND

Save the ssd1306 Sketch to your Device. 

Open the oled_init Sketch and click the green arrow
You should see "Hello World" if not
    - Check your connections
    - Make sure your screen is good
    - the ssd1306 sketch is saved TO THE DEVICE BEFORE 
    RUNNING THE OLED_INIT SKETCH


Joystick Module
Pin Outs 
    - SW -> GPIO 28
    - VRy -> GPIO 27
    - VRx -> GPIO 26
    - VCC -> 3.3v
    - GND -> GND

Open the "joystick.py" sketch and press the green arrow.
Here in the Serial Shell you will see voltages as "coordinates".
The code is set so "down" is the pins.

Troubleshooting
    - make sure you SW pin is not in the GND
    - add a varince into the code to account for errors
        - (this is in the main code as an example and can be copied to here for fine turning)


Buttons and LED
For led pinouts connect one leg of the resister to
a blank leg of the breadboard and the other to the leg
of the LED. I recommend looking up a diagram if this is 
your first time working with and LED. https://sl.bing.net/fyaGc6bb9WK

    - Red LED -> GPIO 17
    - Blue LED -> GPIO 18
Button Modules
Pin outs
    - (red)S -> GPIO 19
    - (blue)S -> GPIO 20
    - (both)VCC-> 3.3v
    - (both) GND -> GND

Open the "led_buttons.py" sketch and press the green arrow.
    - each button should light up their resptive lights
    - make sure your LED legs are in the correct way
    - If a light stays on after you have depressed a button,
    add this after the print statement and before else.
        - time.sleep(.15)
        - led_(color).off()

Rotary Dial
Pin Outs
    - CLK -> GPIO 14
    - DT -> GPIO 15
    - SW -> GPIO 16
    - VCC/+ -> 3.3v
    - GND -> GND

Turn the Rotar Dial and you should see numbers go up and down
based on the way you turn the dial.

    Toubleshooting
        - Make sure you are wired correctly

Bread Board Bored Game

Open the file that named "simon_says.py"
Make sure the sketch ssd1306 is saved to your device.
Press the green arrow.

On the OLED screen an instruction will flash for 2 seconds,
This is randomly chosen by the computer. Each level the computer
randomly chooses another model to add to the instructions.
Possibilities are
Led button push
Rotary Turn (randomly chosen between 1-10)
A joystick direction (Randomly chosen up,down,left or right)

PROBLEMS
    - input window timing
        - you must be holding the action of hit it at the precise time
        for the computer to accept it
    - Rotary dial
        - with the input timing this makes the Rotary dial impossible past
        2
    - Joystick Recentering
        - After pushing a jostick direction, it receives a second input of 
        the opposite direction, this can cause a second input and end the game
    - Not chaining instruction
        - there is an instruction then input, they are not chaining even as levels
        are increasing.

--------------- Version 1.1 -----------------------

Problems adressed

-Timing input windows increased slightly
-Rotary Dial no longer chooses a number, just looks for a "turn" input

Still problems
- joystick recentering
- chaining instructions

import math
import microbit
from microbit import *

# microbit SOP - Flash, REPL, Reset (button near jack on the mircobit.
# Remember to be in microbit mode

while True:
    microbit.sleep(250)
    print(microbit.accelerometer.get_values())
    y = microbit.accelerometer.get_y()
    #Want these values for atan2()
    x = microbit.accelerometer.get_x()
    orientation = ((math.atan2(y, x))/(math.pi))*180
    print(orientation)
    #want this relationship to find angles
    while True:
        if orientation < -90:
            display.show(Image.ARROW_NW)
        elif orientation > -90 and orientation < -15:
            display.show(Image.ARROW_NE)
        elif orientation > 90:
            display.show(Image.ARROW_SW)
        elif orientation < 90 and orientation > 15:
            display.show(Image.ARROW_SE)
        else:
            display.show(Image("00000:00900:09990:00900:00000"))

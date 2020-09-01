""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    potentiometer = 0;
    ultrasonic_ranger = 4
    grovepi.pinMode(potentiometer,"INPUT")

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        sensor_value = grovepi.analogRead(potentiometer)
        ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_ranger)
        if ultrasonic_value <= sensor_value:
        	setText(sensor_value + "  " + "OBJ PRES")
       	else:
       		setText(sensor_value)

       	set_cursor(1, 0)
       	write_text(ultrasonic_value)	

        print(grovepi.ultrasonicRead(PORT))
        time.sleep(0.2)

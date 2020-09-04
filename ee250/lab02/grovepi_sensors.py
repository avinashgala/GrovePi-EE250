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
    setRGB(0,128,64)

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        sensor_value = grovepi.analogRead(potentiometer)
        #This was simply printed to the console for testing purposes
        #print ("sensor_value = %d" % sensor_value)
        sensorstring = str(sensor_value)

        ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_ranger)
        #print(grovepi.ultrasonicRead(PORT))
        ultrastring = str(ultrasonic_value)

        if ultrasonic_value <= sensor_value:
            #this if else only exists so that the formatting looks good on the lcd when there is a 
            #1/2/3/4 digit number for the potentiometer value, because it shifts everything over normally and looks ugly
            if sensor_value <= 9:
                setText_norefresh(sensorstring + " " + "OBJ PRES" + "\n" + ultrastring)
            elif sensor_value <= 99:
                setText_norefresh(sensorstring + "  " + "OBJ PRES" + "\n" + ultrastring)
            elif sensor_value <= 999:
                setText_norefresh(sensorstring + "   " + "OBJ PRES" + "\n" + ultrastring)
            else:
                setText_norefresh(sensorstring + "    " + "OBJ PRES" + "\n" + ultrastring)
        else:
            setText_norefresh(sensorstring + "          " + "\n" + ultrastring)
        #print ("sensor_value = %d" % sensor_value)
        
        time.sleep(0.2)
    
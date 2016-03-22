#!/usr/bin/python

# Import required Python libraries
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)


# Define GPIO to use on Pi
GPIO_OUT = 2


print "Light Control"


# Set pins as output and input
#GPIO.setup(GPIO_IN,  GPIO.IN)
GPIO.setup(GPIO_OUT, GPIO.OUT)


b = True
while True:
	if b:
		print("Light Power ON")
		GPIO.output(GPIO_OUT, True)
		b = False
	else:
		print("Light Power OFF")
		GPIO.output(GPIO_OUT, False)
		b = True
	time.sleep(1.0)
# Reset GPIO settings
GPIO.cleanup()

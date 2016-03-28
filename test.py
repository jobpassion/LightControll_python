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
GPIO.setup(3, GPIO.OUT)


b = True
i = 0
while True:
    inputStr = raw_input('Please enter your input:')
    if inputStr == 'open':
    #if b:
    #if i % 3 != 0:
        print("Light Power ON")
        GPIO.output(GPIO_OUT, False)
        b = False
    elif inputStr == 'high':
        print("Light Power High")
        GPIO.output(3, False)
    elif inputStr == 'low':
        print("Light Power Low")
        GPIO.output(3, True)
    elif inputStr == 'close':
        print("Light Power OFF")
        GPIO.output(GPIO_OUT, True)
        b = True
    i = i + 1
    time.sleep(1.0)
# Reset GPIO settings
GPIO.cleanup()

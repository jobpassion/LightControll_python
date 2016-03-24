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
i = 0
def switch(isOpen):
    #self.b = isOpen
    GPIO.output(GPIO_OUT, isOpen)
    switch.status = isOpen
def status():
    return switch.status
def apply():
    print("Light Power ON" + b)
    if b:
        GPIO.output(GPIO_OUT, True)
    else:
        GPIO.output(GPIO_OUT, False)
        
#while True:
#        inputStr = raw_input('Please enter your input:')
#        if inputStr == 'open the light':
#        #if b:
#        #if i % 3 != 0:
#                print("Light Power ON")
#                GPIO.output(GPIO_OUT, True)
#                b = False
#        else:
#                print("Light Power OFF")
#                GPIO.output(GPIO_OUT, False)
#                b = True
#        i = i + 1
#        time.sleep(1.0)
# Reset GPIO settings
#GPIO.cleanup()

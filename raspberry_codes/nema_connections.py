import RPi.GPIO as GPIO
import time

#------------------ Set up GPIO ------------------
#Nema23
GPIO.setmode(GPIO.BCM)
dir_pin23z = 21        # pin 40
pul_pin23z = 20        # pin 38

GPIO.setup(dir_pin23z, GPIO.OUT)
GPIO.setup(pul_pin23z, GPIO.OUT)

#Nema17 x
dir_pin17x = 23       # pin 16
pul_pin17x = 12       # pin 32
GPIO.setup(dir_pin17x, GPIO.OUT)
GPIO.setup(pul_pin17x, GPIO.OUT)

#Nema17 y
dir_pin17y = 
pul_pin17y = 
GPIO.setup(dir_pin17y, GPIO.OUT)
GPIO.setup(pul_pin17y, GPIO.OUT)
#--------------------------------------------------


# dir = 1 is clockwise
# dir = 0 is anti-clockwise
def moveZ(dir,units):   
    try:
        GPIO.output(dir_pin23z, dir) 
        while units :
            # starting pulse with 1
            GPIO.output(pul_pin23z,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pul_pin23z,GPIO.LOW)
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) or other exceptions
        GPIO.cleanup()


def moveX(dir,units):
    try:
        GPIO.output(dir_pin17x, dir) 
        while units :
            # starting pulse with 1
            GPIO.output(pul_pin17x,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pul_pin17x,GPIO.LOW)
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) or other exceptions
        GPIO.cleanup()
        
        
def moveY(dir,units):
    try:
        GPIO.output(dir_pin17y, dir) 
        while units :
            # starting pulse with 1
            GPIO.output(pul_pin17y,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pul_pin17y,GPIO.LOW)
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) or other exceptions
        GPIO.cleanup()
             

def exitGPIO():
# Clean up GPIO on program exit
    GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

def signal_handler(signal, frame):
	print ('You entered Ctrl+C!')
	GPIO.output(33, GPIO.LOW)
	GPIO.output(35, GPIO.LOW)
	GPIO.output(37, GPIO.LOW)
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


dirPin0 = 33
dirPin1 = 35

stepPin = 37

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

GPIO.setup(dirPin0, GPIO.OUT)   # Set dirPin to output
GPIO.setup(dirPin1, GPIO.OUT)  # Set stepPin to output
GPIO.setup(stepPin, GPIO.OUT)

#Amount to turn

#degrees = 360


#1 = counter clockwise
#0 = clockwise 

dir = input("Which direction? ")

if (dir == 1):
	GPIO.output(dirPin0, GPIO.HIGH)
	GPIO.output(dirPin1, GPIO.LOW)
	print "turning l"

elif (dir == 0):
	GPIO.output(dirPin0, GPIO.LOW)
	GPIO.output(dirPin1, GPIO.HIGH)
	print "turning r"


degrees = input("Enter number of degrees: ")
delay = input("From 1-5, enter how fast you want to spin: ")

if (delay == 1):
    delay = 0.6
    
elif (delay == 2):
    delay = 0.20
    
elif (delay == 3):
    delay = 0.01
    
elif (delay == 4):
    delay = 0.0025
    
elif (delay == 5):
    delay = 0.001

spr = 50

#Calculate steps to take
stepCount = int(degrees / 90) *spr

#Perform turn, 20 is our step pin
for i in range(stepCount):
    print "step ", i
    sleep(delay)
    GPIO.output(stepPin, GPIO.LOW)
    sleep(delay)
    GPIO.output(stepPin, GPIO.HIGH)



GPIO.output(stepPin, GPIO.LOW)
GPIO.output(dirPin0, GPIO.LOW)
GPIO.output(dirPin1, GPIO.LOW)

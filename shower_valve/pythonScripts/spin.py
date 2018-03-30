import RPi.GPIO as GPIO
from time import sleep

dirPin = 33
stepPin = 37

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

GPIO.setup(dirPin, GPIO.OUT)   # Set dirPin to output
GPIO.setup(stepPin, GPIO.OUT)  # Set stepPin to output

GPIO.output(dirPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led


#Amount to turn

#degrees = 360


#1 = counter clockwise
#0 = clockwise

GPIO.output(stepPin, GPIO.HIGH)  #controlls direction of motor
 


dir = input("Which direction? ")
GPIO.output(dirPin, dir)  #controlls direction of motor
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


#This variable is dependent on your motor
#spr = 360/step angle (ours is 1.8) ---so is ours, Weida (see bottom of our motor)
spr = 50   #  DO NOT CHANGE VALUE

#Calculate steps to take
stepCount = int(degrees / 90) *spr     #this value == number of degrees sup
#delay = 0.01                        #DECREASE this value to spin FASTER

#Perform turn, 20 is our step pin
for i in range(stepCount):
    print "step ", i
    sleep(delay)
    GPIO.output(stepPin, GPIO.LOW)
    sleep(delay)
    GPIO.output(stepPin, GPIO.HIGH)



GPIO.output(stepPin, GPIO.LOW)
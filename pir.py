#  MBTechWorks.com 2017
#  Use an HC-SR501 PIR to detect motion (infrared)

#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import pygame 


#load music

pygame.mixer.init()
pygame.mixer.music.load("Dueling Banjos.mp3")
#setup GPIO pin
GPIO.setmode(GPIO.BOARD)            #Set GPIO to pin numbering
pir = 12                           #Assign pin 8 to PIR
GPIO.setup(pir, GPIO.IN)#setup pulldown resistor


print ("Sensor initializing . . .")
time.sleep(2)                       #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")

while (1):
    if GPIO.input(pir) and (not pygame.mixer.music.get_busy()):
        print("input was high")
        pygame.mixer.music.play(0, 120)
    else:
        print("input was low")

    time.sleep(2)
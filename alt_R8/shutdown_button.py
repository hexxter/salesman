#! /usr/bin/env python
import os
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(5, GPIO.IN)

try:
	while True:
		if not (GPIO.input(5)):
			GPIO.output(7, False)
			time.sleep(.1)
			GPIO.output(7, True)
			time.sleep(.1)
			GPIO.output(7, False)
			time.sleep(.1)
			GPIO.output(7, True)
			
			os.system("/sbin/shutdown -h now")
		time.sleep(.5)
except:
	GPIO.cleanup()

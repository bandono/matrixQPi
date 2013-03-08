#!/usr/bin/python
import wiringpi
import time
INPUT=0
OUTPUT=1

SETUP=wiringpi.wiringPiSetup()
print SETUP
wiringpi.pinMode(7,INPUT)

RESULT=wiringpi.digitalRead(7)
while RESULT==1:
	RESULT=wiringpi.digitalRead(7)
	time.sleep(1)
print RESULT

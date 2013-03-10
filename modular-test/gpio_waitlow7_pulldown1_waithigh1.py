#!/usr/bin/python
import wiringpi
import time
INPUT=0
OUTPUT=1
HIGH=1
LOW=0

SETUP=wiringpi.wiringPiSetup()
print SETUP
wiringpi.pinMode(7,INPUT)
wiringpi.pinMode(1,OUTPUT)
wiringpi.digitalWrite(1,LOW)

RESULT=wiringpi.digitalRead(7)
while RESULT==1:
	RESULT=wiringpi.digitalRead(7)
	time.sleep(1)
print RESULT

wiringpi.pinMode(1,INPUT)
wiringpi.pinMode(7,OUTPUT)
wiringpi.digitalWrite(7,HIGH)

RESULT=wiringpi.digitalRead(1)
while RESULT==0:
        RESULT=wiringpi.digitalRead(1)
        time.sleep(1)
print RESULT


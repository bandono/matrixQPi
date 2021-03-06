#!/usr/bin/python
# version 1.0
# read 3x4 membrane keypad and print pressed key to stdout
# command line argument:
# -i : light a LED for 1 seconds indicating successful pressed key reading

import wiringpi
import time
import sys
INPUT=0
OUTPUT=1
HIGH=1
LOW=0

#mapping of used GPIO for LED indicator
led=1

# getting command line argument if any
try:
	myArg=sys.argv[1]
except:
	# if no argument, assign 0 to myArg
	myArg=0

def turnOnLED():
	wiringpi.pinMode(led,OUTPUT)
	wiringpi.digitalWrite(led,LOW)
	time.sleep(1)
	wiringpi.pinMode(led,INPUT)

# mapping of symbols from the keypad button 
# keypad used below is like phone dial key (10 digits and "*", "#" signs)
keyPad=[
[1,2,3],
[4,5,6],
[7,8,9],
["*",0,"#"]
]

# mapping of used GPIO pin in wiringPi numbering to rows and columns
row=[7,0,2,3]
col=[4,5,6]

SETUP=wiringpi.wiringPiSetup()
# for debugging we can print SETUP status
# print SETUP

# (1) set all columns as output low
for j in range(len(col)):
	wiringpi.pinMode(col[j],OUTPUT)
	wiringpi.digitalWrite(col[j],LOW)

# (2) set all rows as input
for i in range(len(row)):
	wiringpi.pinMode(row[i],INPUT)

# (3) scan rows for pushed key/button
rowHi=1
while rowHi==1:
	for i in range(len(row)):
		tmpRead=wiringpi.digitalRead(row[i])
		if tmpRead==0:
			rowHi=0
			rowVal=i

# (4) after finding which key/button from the row scans, convert columns to input
for j in range(len(col)):
        wiringpi.pinMode(col[j],INPUT)

# (5) switch the i-th row found from scan to output
wiringpi.pinMode(row[rowVal],OUTPUT)
wiringpi.digitalWrite(row[rowVal],HIGH)

# (6) scan columns for still-pushed key/button
colLo=0
while colLo==0:
        for j in range(len(col)):
                tmpRead=wiringpi.digitalRead(col[j])
                if tmpRead==1:
                        colLo=1
			colVal=j

# (7) print the symbol of pressed key, note that it prints newline 
print keyPad[rowVal][colVal]

# (7) reinitialize all rows and columns as input before exiting
for i in range(len(row)):
        wiringpi.pinMode(row[i],INPUT) 
for j in range(len(col)):
        wiringpi.pinMode(col[j],INPUT)

if myArg=="-i":
	turnOnLED()
	sys.exit()
else:
	sys.exit()

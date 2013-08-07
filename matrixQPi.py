import wiringpi
import time

INPUT=0
OUTPUT=1
HIGH=1
LOW=0

class matrixQConst:
	def __init__(self):
		# mapping of used GPIO pin in wiringPi numbering to rows and columns
		self.row=[7,0,2,3]
		self.col=[4,5,6]
		#mapping of used GPIO for LED indicator
		self.led=1
		self.defaultKeyPad=[
			[1,2,3],
			[4,5,6],
			[7,8,9],
			["*",0,"#"]
		]
	
class matrixQPi(object):
	"""Simple matrix key row-column GPIO reader"""
	# mapping of symbols from the keypad button
	# default optional keypad with phone dial keys (10 digits and "*", "#" signs)
	default =  matrixQConst()

	def __init__(self, numberOfRow=4, numberOfCol=3, keyPad=default.defaultKeyPad, row=default.row, col=default.col):
		self.SETUP=wiringpi.wiringPiSetup()

		# (1) set all columns as output low
		for j in range(len(col)):
			wiringpi.pinMode(col[j],OUTPUT)
			wiringpi.digitalWrite(col[j],LOW)

		# (2) set all rows as input
		for i in range(len(row)):
			wiringpi.pinMode(row[i],INPUT)
		
		self.keyPad = keyPad
		self.row = row
		self.col = col

	def turnOnLED(self):
		wiringpi.pinMode(led,OUTPUT)
		wiringpi.digitalWrite(led,LOW)
		time.sleep(1)
		wiringpi.pinMode(led,INPUT)
        
	def reInit(self):
		# reinitialize all rows and columns as input before exiting
		for i in range(len(self.row)):
			wiringpi.pinMode(self.row[i],INPUT)
		for j in range(len(self.col)):
			wiringpi.pinMode(self.col[j],INPUT)

	def scanQ(self):
		# (3) scan rows for pushed key/button
		rowHi=1
		while rowHi==1:
			for i in range(len(self.row)):
				tmpRead=wiringpi.digitalRead(self.row[i])
				if tmpRead==0:
					rowHi=0
					rowVal=i

		# (4) after finding which key/button from the row scans, convert columns to input
		for j in range(len(self.col)):
				wiringpi.pinMode(self.col[j],INPUT)

		# (5) switch the i-th row found from scan to output
		wiringpi.pinMode(self.row[rowVal],OUTPUT)
		wiringpi.digitalWrite(self.row[rowVal],HIGH)

		# (6) scan columns for still-pushed key/button
		colLo=0
		while colLo==0:
				for j in range(len(self.col)):
						tmpRead=wiringpi.digitalRead(self.col[j])
						if tmpRead==1:
							colLo=1
							colVal=j

		# (7) print the symbol of pressed key, note that it prints newline
		return self.keyPad[rowVal][colVal]
		
		reInit()
		#if myArg=="-i":
        #turnOnLED()

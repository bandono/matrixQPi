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
	"""Simple matrix key row-column GPIO reader
	   Attributes: 
	"""
	# mapping of symbols from the keypad button
	# default optional keypad with phone dial keys (10 digits and "*", "#" signs)
	default =  matrixQConst()

	def __init__(self, numberOfRow=4, numberOfCol=3, keyPad=default.defaultKeyPad, row=default.row, col=default.col):
		# wiringPi instance creation
		# (print SETUP for debugging, success value is SETUP=1) 
		self.SETUP=wiringpi.wiringPiSetup()
		
		# in class 'global' constants
		self.keyPad = keyPad
		self.row = row
		self.col = col

	def turnOnLED(self,onDuration):
		wiringpi.pinMode(led,OUTPUT)
		wiringpi.digitalWrite(led,LOW)
		time.sleep(onDuration)
		wiringpi.pinMode(led,INPUT)
		
	def __preRead(self):
		# (1) set all columns as output low
		for j in range(len(self.col)):
			wiringpi.pinMode(self.col[j],OUTPUT)
			wiringpi.digitalWrite(self.col[j],LOW)

		# (2) set all rows as input
		for i in range(len(self.row)):
			wiringpi.pinMode(self.row[i],INPUT)
			       
	def __postRead(self):
		# reinitialize all rows and columns as input before exiting
		for i in range(len(self.row)):
			wiringpi.pinMode(self.row[i],INPUT)
		for j in range(len(self.col)):
			wiringpi.pinMode(self.col[j],INPUT)

	def scanQ(self):
		# steps (1) and (2) before reading GPIOs
		self.__preRead()
		
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

		# reinitialize used GPIOs
		self.__postRead()

		# (7) return the symbol of pressed key from keyPad mapping
		return self.keyPad[rowVal][colVal]

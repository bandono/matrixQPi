#!/usr/bin/python

# example_2x2.py
# an example on how to use the matrixQPi class
# to read input from matrix keypad
# and print the returned button symbol
#
# 2 x 2 keypad is used in this example
# below is the visual layout of the buttons:
#
# ---------
# | 2 | 3 | 
# ---------
# | 5 | 6 | 
# ---------
#
# requires: matrixQPi.py in same path
# usage (as root): $ python example.py

from matrixQPi import *

# keypad button symbol mapping
keyPad=[[2, 3],
        [5, 6]
]

# GPIO addresses used in my version of 4 x 3 circuitry are 
# row=[7,0,2,3]
# col=[4,5,6]
#
# used GPIO address, logically grouped as row and column
# for the above buttons (2 x 2 matrix)
row=[7, 0]
col=[5, 6]

# our keypad intance
QPad  = matrixQPi(keyPad=keyPad,row=row,col=col)

# print reading of pressed-button
# (reading one pressed-key at a time)
print QPad.scanQ()

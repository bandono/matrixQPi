#!/usr/bin/python

# example_4x3.py
# an example on how to use the matrixQPi class
# to read input from matrix keypad
# and print the returned button symbol
#
# 4 x 3 keypad is used in this example
# below is the visual layout of the buttons:
#
# ------------
# | 1 | 2 | 3 |
# ------------
# | 4 | 5 | 6 |
# ------------
# | 7 | 8 | 9 |
# -------------
# | * | 0 | # |
# -------------
#
# requires: matrixQPi.py in same path
# usage (as root): $ python example.py

from matrixQPi import *

# keypad button symbol mapping
keyPad=[[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
        ['*', 0, '#']
]

# GPIO addresses used in my version of 4 x 3 circuitry are
# row=[7,0,2,3]
# col=[4,5,6]
#
# when all used mapped to 4 x 3 buttons keypad:
row=[7,0,2,3]
col=[4,5,6]

# our keypad intance
QPad  = matrixQPi(keyPad=keyPad,row=row,col=col)

# print reading of pressed-button
# (reading one pressed-key at a time)
print QPad.scanQ()

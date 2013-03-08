matrixQPi
=========

matrixQPi (Matrix Keypad for Raspberry Pi): a wiringPi-based code for reading input from membrane keypad (matrix keypad) comes in 3x4 buttons

Run reading by:
`$ python matrixQPi` 

It can only read one pressed key at a time.

It will print the symbol of the pressed key found from the lookup. In this case the lookup contains symbols from regular phone dial-in key (digits 0, 1,..., 9 plus * and # signs)

As already stated above this requires wiringPi (`https://github.com/WiringPi/WiringPi-Python`) library. It has already tested using Raspberry Pi with Python 2.7.3rc2.

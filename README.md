matrixQPi
=========

matrixQPi (Matrix Keypad for Raspberry Pi): a WiringPi-Python-based code for 
reading input from membrane keypad (matrix keypad) comes in 4x3 buttons.

`matrixQPi_stdout.py` is an example that will print pressed-button to `stdout`

Calling the above script in a bash loop will print pressed-button repetitively:
`$ while true; do matrixQPi_stdout.py -i; done` 

It basically reads one pressed key at a time, the above bash loop only repeats
the reading

It will print the symbol of the pressed key found from the lookup. In this case 
the lookup contains symbols from regular phone dial-in key (digits 0, 1,..., 9
plus * and # signs)

As already stated above this requires [WiringPi-Python] [1] installed to the
Raspberry Pi as library. However, since this library is already deprecated,
you should use [WiringPi-Python@9c77bde] [2] commit. Hence, the library's 
submodule can't also be used from calling `git submodule update --init`.

You must copy manually [WiringPi@89bbe97] [3] commit, putting them under
`WiringPi` directory of the `WiringPi-Python`. Once you have both correct 
tree from Github, install the working version of this library then using
`$ sudo python setup.py install`

This has already tested using Raspberry Pi with Python 2.7.3rc2.

  [1]: https://github.com/WiringPi/WiringPi-Python "WiringPi-Python"
  [2]: https://github.com/WiringPi/WiringPi-Python/tree/9c77bde53fb5fa6283268b4a529e47048f8a379d "WiringPi-Python@9c77bde"
  [3]: https://github.com/WiringPi/WiringPi/tree/89bbe97856407979fa75c4c793fabf4db839a0ee "WiringPi@89bbe97"


matrixQPi Class
===============

The class provides flexibility to use different matrix keypad size and symbol
mapping as well as GPIO pins assigned for reading.

Check `exampleXXX.py` on how to use the class in practice. In general you need
to define:
 * Button symbol character
 * GPIO used as logical row and column of the matrix
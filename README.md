[![License: MIT][image-1]][1]

# Chip-8
🕹️ A Chip-8 emulator written in Python 3!

> [Chip-8][2] is a simple, interpreted, programming language which was first used on some do-it-yourself computer systems in the late 1970s and early 1980s.

## Motivation

My main motivation is to increase familiarity with the Python 3 language and to learn lower level programming concepts.

Here are only some concepts I learned while writing this emulator:
- How to disassemble and decode an opcode into instructions a CPU can use.
 - How a CPU can utilise memory, stack, program counters, stack pointers, memory addresses, and registers.
- How a CPU implements fetch, decode, and execute.

## Key Mappings
This dictionary is organised to resemble the 1977 COSMAC VIP's keyboard which had a 16-key hexadecimal keypad.

	  Chip-8   Interpreter
	|1|2|3|C|   |1|2|3|4|
	|4|5|6|D|   |Q|W|E|R|
	|7|8|9|E|   |A|S|D|F|
	|A|0|B|F|   |Z|X|C|V|


## Acknowledgements

- [CHIP-8 Wikipedia][3]
- [Cowgod's Chip-8 Technical Reference][4]
- [Laurence Muller’s introduction to the world of emulation][5] 

## Author

- Alexander Schroll

## License

This project is open source and available under the [MIT License][6].

[1]:	https://opensource.org/licenses/MIT
[2]:	https://en.wikipedia.org/wiki/CHIP-8
[3]:	https://en.wikipedia.org/wiki/CHIP-8
[4]:	http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
[5]:	http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter
[6]:	LICENSE

[image-1]:	https://img.shields.io/badge/License-MIT-blue.svg
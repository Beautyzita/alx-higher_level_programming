#!/usr/bin/python
for letter in range(97, 123):
    if shr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")

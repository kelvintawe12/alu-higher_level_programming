#!/usr/bin/python3
#Write a python program that prints the ASCII alphabet, in lowercase, not followed by a new line.
for i in range(97, 123):
    print("{}".format(chr(i)), end='')

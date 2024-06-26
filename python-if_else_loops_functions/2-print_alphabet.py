#!/usr/bin/python3

# Write a Python program that prints the ASCII alphabet in lowercase,
# without a newline, using only one print function and one loop.

for i in range(97, 123):
    print("{}".format(chr(i)), end='')

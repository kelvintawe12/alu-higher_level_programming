#!/usr/bin/python3

# Print the lowercase ASCII alphabet, excluding 'q' and 'e'
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end='')

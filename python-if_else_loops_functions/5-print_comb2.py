#!/usr/bin/python3

# Print numbers from 0 to 99
for i in range(100):
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')

#!/usr/bin/python3

def uppercase(s):
    print("".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s))

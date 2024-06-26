#!/usr/bin/python3

def get_unicode_code_point(c):
    """
    Returns the Unicode code point of the given character.
    """
    return ord(c)

# Example usage:
print(get_unicode_code_point('a'))  
print(get_unicode_code_point('\u2020'))

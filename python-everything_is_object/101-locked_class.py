#!/usr/bin/python3
"""this module will be used to execute a ,ajority of code,"""


class LockedClass:
    """this is a simple class for the code which is to displlay thr str"""
    def __setattr__(self, attr, value):
        if not hasattr(self, 'first_name') and attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(attr))
        super().__setattr__(attr, value)

if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except AttributeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

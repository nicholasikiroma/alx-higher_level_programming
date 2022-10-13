#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside Result: {}".format(a))
    return a

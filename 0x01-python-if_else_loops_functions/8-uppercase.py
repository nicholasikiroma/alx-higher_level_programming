#!/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print(f"{c:s}", end = '')
    print("")

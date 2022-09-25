#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    add = 0
    for n in argv[1:]:
        add += int(n)
    print("{:d}".format(add))

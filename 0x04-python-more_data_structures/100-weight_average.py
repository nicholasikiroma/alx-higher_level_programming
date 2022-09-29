#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        dem = 0
        for item in my_list:
            num += (item[0] * item[1])
            dem += item[1]
        return (num / dem)
    return 0
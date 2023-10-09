#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_list = []
    for i in my_list:
        if (i % 2 == 0):
            mul_list.append(True)
        else:
            mul_list.append(False)
    return (mul_list)

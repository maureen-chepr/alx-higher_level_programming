#!/usr/bin/python3
if __name__ == '__main__':
from calculator_1 import add, sub, mul, div
a = 10
b = 5
value_add = add(a, b)
value_sub = sub(a, b)
value_mul = mul(a, b)
value_div = div(a, b)
print("{:d} + {:d} = {:d}".format(a, b, value_add))
print("{:d} - {:d} = {:d}".format(a, b, value_sub))
print("{:d} * {:d} = {:d}".format(a, b, value_mul))
print("{:d} / {:d} = {:d}".format(a, b, value_div))

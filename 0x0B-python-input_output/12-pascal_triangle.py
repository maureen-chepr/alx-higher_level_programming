#!/usr/bin/python3
"""
    pascal triangle module
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    result = []
    my_list = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(my_list[y] + my_list[y - 1])
        my_list = row
        result.append(row)
    return result

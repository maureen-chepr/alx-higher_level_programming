#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(arr):
    """
    Find the peak element in a list.
    """
    if not arr:
        return None

    n = len(arr)

    if n == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]

    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]

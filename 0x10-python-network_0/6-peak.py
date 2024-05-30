#!/usr/bin/python3
"""
function that finds peak in alist of integers
"""


def find_peak(list_of_integers):
    """
    looks for peak in unsorted list
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        middle = (left + right) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1}:
            right = middle
        else:
            left = middle + 1
    return list_of_integers[left]

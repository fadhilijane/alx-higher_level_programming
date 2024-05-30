#!/usr/bin/python3
"""
function that finds peak in alist of integers
"""

def find_peak(list_of_integers):
   """looks for peak"""
   if not list_of_integers:
       return None

   list_left, list_right = 0, len(list_of_integers) - 1
   while list_left < list_right:
       middle = (list_left + list_right) // 2

       if list_of_integers[middle] > list_of_integers[middle + 1}:
           list_right = middle
        else:
            list_left = middle +1
    return list_of_integers[list_left]

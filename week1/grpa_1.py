"""
Write a function find_Min_Difference(L, P) that accepts a list L of integers and
P (positive integer) where the size of L is greater than P. The task is to pick P different elements from
the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared
to other differences in possible subset of p elements. The function returns this minimum difference value.

Note - The list can contain more than one subset of p elements that have the same minimum difference value.
"""

import math


def find_Min_Difference(L, P):
    min_diff = math.inf
    sorted_L = sorted(L)

    i = 0
    while i + P - 1 <= len(sorted_L) - 1:
        diff = sorted_L[i + P - 1] - sorted_L[i]
        min_diff = min(diff, min_diff)
        i += 1

    return min_diff


L = [3, 4, 1, 9, 56, 7, 9, 12]
P = 5
print(find_Min_Difference(L, P))

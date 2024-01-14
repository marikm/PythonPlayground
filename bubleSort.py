#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    i: int = 0
    j: int = 0
    swap: int = 0
    while i < len(a) - 1:
        j = i + 1
        while j <= len(a) - 1:
            if a[i] > a[j]:
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
                j = j + 1
                swap = swap + 1
            else:
                j = j+1
        i = i + 1
    return swap


if __name__ == '__main__':
    n = int(input().strip())  # 3

    a = list(map(int, input().rstrip().split()))

    n = countSwaps(a)
    x: int = len(a) - 1

    print("Array is sorted in " + str(n) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[x]))

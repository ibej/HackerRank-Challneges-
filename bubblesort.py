#!/bin/python3

import math
import os
import random
import re
import sys

# Author: HackerRank
# Author: Ian Bejarano (countSwaps() function)
# Date: 4/17/2023

# Complete the 'countSwaps' function below.
# The function accepts INTEGER_ARRAY a as parameter.

def countSwaps(a):
    numSwaps = 0
    n = len(a)
    for i in range(0, n): 
        for j in range(0, n-1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]: 
                placeHolder = a[j] # placeholder variable to save the soon to be lost array value
                a[j] = a[j+1] # swap 1/2
                a[j+1] = placeHolder # swap 2/2
                numSwaps += 1 # increase the counter
    
    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
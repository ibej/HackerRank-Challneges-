#!/bin/python3

import math
import os
import random
import re
import sys

# Author: HackerRank
# Author: Ian Bejarano (plusMinus() function)
# Date: 4/11/2023

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    n = len(arr)
    pos = 0; neg = 0; neut = 0
    for x in arr:
        if x == 0 : neut+=1
        elif x > 0 : pos+=1
        elif x < 0 : neg+=1
    
    print(f'{pos/n:.6f}')
    print(f'{neg/n:.6f}')
    print(f'{neut/n:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
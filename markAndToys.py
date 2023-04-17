#!/bin/python3

import math
import os
import random
import re
import sys

# Author: HackerRank
# Author: Ian Bejarano (maximumToys() function)
# Date: 4/17/2023

# Complete the 'maximumToys' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k

def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    bill = 0
    numToys = 0
    for price in sortedPrices:
        if bill + price <= k:
            bill += price
            numToys += 1
    
    return numToys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

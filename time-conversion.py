#!/bin/python3

import math
import os
import random
import re
import sys

# Author: HackerRank
# Author: Ian Bejarano (timeConversion() function)
# Date: 4/10/2023

# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    splitted = s.split(':')
    
    if s[-2: ] == 'AM':
        if splitted[0] == '12':
            splitted[0] = '00'
        
        return splitted[0] + ':' + splitted[1] + ':' + splitted[2][0:2]
    
    elif s[-2: ] == 'PM':
        if splitted[0] != '12':
            hrs = str(int(splitted[0]) + 12)
            mins = splitted[1]
            secs = splitted[2][0:2]
            return hrs + ':' + mins + ':' + secs
        else:
            return splitted[0] + ':' + splitted[1] + ':' + splitted[2][0:2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
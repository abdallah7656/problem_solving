#!/bin/python3

import math
import os
import random
import re
import sys
 
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

# Function Description

# Complete the function birthdayCakeCandles 

# birthdayCakeCandles has the following parameter(s):

# int candles[n]: the candle heights
# Returns
# int: the number of candles that are tallest

# Sample Input 
# 4
# 3 2 1 3
# Sample Output 
# 2

# def birthdayCakeCandles(candles):
#     freq={}
#     num=1
#     tallest =max(candles)
#     for i in candles:
#         freq[i]=num+1
#     return freq[tallest]
    
from typing import List

def birthdayCakeCandles(candles: List[int]) -> int:
    max_height = max(candles)
    return candles.count(max_height)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

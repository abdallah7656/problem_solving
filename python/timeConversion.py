#!/bin/python3

import math
import os
import random
import re
import sys

#
#  
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # extract the hour, minute, second, and period (AM/PM) from the input string
    hour = int(s[0:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    period = s[8:10]

    # convert the hour to 24-hour format if necessary
    if period == 'PM' and hour < 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    # format the time in 24-hour format and return the result
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

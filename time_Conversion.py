#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    #First check if time given is AM or PM
    check_AM_PM=s[-2:]
    # print(s[:2])
    print(check_AM_PM)
    if check_AM_PM=="AM":
        if s[:2]=="12":
            return "00"+s[2:-2]
        else:
            return s[:-2]
    
    else:
        if s[:2]=="12":
           return s[:-2]
        else:
           HH=int(s[:2])+12
           return str(HH)+s[2:-2]


    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
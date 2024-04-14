#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr=sorted(arr)
    min_sum=str(sum(arr[:-1]))
    max_sum=str(sum(arr[1:]))
    print(min_sum+" "+max_sum)

    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
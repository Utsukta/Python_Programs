#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for i in range(len(apples)):
      apple_dist=apples[i]+a
      if s<=apple_dist<=t:
        apple_count=apple_count+1
    print(apple_count)
      
    for j in range(len(oranges)):
       orange_dist=oranges[j]+b
       if s<=orange_dist<=t:
         orange_count=orange_count+1
    print(orange_count)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    # print(first_multiple_input)

    s = int(first_multiple_input[0])
    # print(s)

    t = int(first_multiple_input[1])
    # print(t)

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    # print(len(apples))

    oranges = list(map(int, input().rstrip().split()))
    # print(oranges)

    countApplesAndOranges(s, t, a, b, apples, oranges)
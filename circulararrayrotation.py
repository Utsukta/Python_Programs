#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # is k is greater than len(a), it means the rotation wraps around the array multiple times.
    # For instance, if len(a) is 5 and k is 7, rotating the array 7 times is equivalent to 
    #rotating it only 2 times (7 % 5 = 2), 
    #as after 5 rotations, you're back to the original array configuration.
    x = k % len(a)
    print(x)
    a = a[-x:] + a[:-x]
    print(a)
    res = []
    for q in queries:
        res.append(a[q])
    return res
  
    b=[]
    for _ in range(k):
        val = a.pop()
        a.insert(0,val)
        # a.pop(len(a))
        print(a)
        # print(a)
    for j in range(len(queries)):
     
     b.append(a[j])

    # return "\n".join(map(str,b))
    




        # queries[i]=a[i]
        # print(qu)

        
        # print(type(val))
        # print(i)

    pass
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    # print(queries)

    result = circularArrayRotation(a, k, queries)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
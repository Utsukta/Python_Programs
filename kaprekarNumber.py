#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    kaprekar_number=[]
    for i in range(p,q+1):
        d=len(str(i))
        sqr=str(i**2)
        sqr_d=len(str(sqr))
        if i==1:
            kaprekar_number.append(i)
        if i>3 and (sqr_d==2*d or sqr_d==(2*d)-1):
            r=sqr[-d:]
            print("right"+r)
            l=sqr[:-d]
            print("left"+l)
            print(int(r)+int(l))
            if(int(r)+int(l))==i:
                kaprekar_number.append(i)
        
    if len(kaprekar_number)==0:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, kaprekar_number)))
   

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
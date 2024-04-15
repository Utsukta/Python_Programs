#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    mat=[]
    k=min(m,n)//2

    for i in range(k):
        temp=[]
        for j in range(i,n-1-i):
            # pass
            temp.append(matrix[i][j])
        # print(temp)
        for j in range(i,m-1-i):
            # pass
            temp.append(matrix[j][n-1-i])
        # print(temp)

        for j in range(n-1-i,i,-1):
            # pass
            temp.append(matrix[m-1-i][j])
        # print(temp)
            
        for j in range(m-1-i,i,-1):
            temp.append(matrix[j][i])
        # print(temp)
        mat.append(temp)
    # print(mat)

    for i in range(k):
        row=mat[i]
        idx=r%len(row)
        def inc():
            return (idx+1)%len(row)
        
        for j in range(i,n-1-i):
            matrix[i][j]=row[idx]
            idx=inc()
            # pass
          
        # print(temp)
        for j in range(i,m-1-i):
            # pass
            matrix[j][n-1-i]=row[idx]
            idx=inc()
        # print(temp)

        for j in range(n-1-i,i,-1):
            # pass
            matrix[m-1-i][j]=row[idx]
            idx=inc()
        # print(temp)
            
        for j in range(m-1-i,i,-1):
            matrix[j][i]=row[idx]
            idx=inc()
        
    for row in matrix:
            print(*row)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    # print(matrix)

    matrixRotation(matrix, r)
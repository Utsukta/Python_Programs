#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # L = len(s)
    # print(L)
    space_removed=s.replace(" ", "")
    L=len(space_removed)
    print(L)
    rows=math.floor(math.sqrt(L))
    colums=math.ceil(math.sqrt(L))
    print(colums)
    print(rows)
    result=[]
    if rows*colums<L:
     rows=rows+1
    else:
     rows=rows
    for i in range(colums):
        temp=[]
        for j in range(rows):
            index=i+j*colums
            #if we add rows then we will go for index out of range so.
            if index<L:
               temp.append(space_removed[index])
               print(temp)
        result.append(''.join(temp))
    return  " ".join(result)


    # for i in range(colums):
    #     temp=[]
    #     j=0
    #     while i+j<L:
    #         temp.append(space_removed[i+j])
    #         print(temp)
    #         j+=colums
    #     result.append("".join(temp))
    #     print(temp)

    # return " ".join(result)
            
        
    # rows = int(math.floor(L**(0.5)))
    
    # output = ""
    # for i in range(columns):
    #     k = i
    #     for j in range(k, L, columns):
    #         output+=s[j]
    #     output+=" "
    # return output
    # space_removed=s.replace(" ", "")
    # L=len(space_removed)
    # # print(L)
    # sq=math.sqrt(L)
    # # print(sq)
    # rows=math.floor(math.sqrt(L))
    # # print(rows)
    # colums=math.ceil(math.sqrt(L))
    # # print(colums)

    
    # my_list=[]
    # for i in range(L):
    #   #Check if new column as started or not
    #   if i%colums==0:
    #     #for iteration 1, i=0
    #     #for iteration 2 i=4 and so on
    #     sub=space_removed[i:i+colums]
        
        
    #     # for j in sub:
    #     my_list.append(sub)
    #     # print(my_list)
    #     # print("".join(my_list))
    #     # print(my_list)
    #     # print(sss)
    # res=[]
    # for c in range(colums):
    #    temp_list=[]
    #    for r in range(rows):
    #       if(rows*colums>L):
    #       # print(r)
    #        temp_list.append(my_list[r][c])
    #       else:
    #          rows=rows+1

    #    res.append("".join(temp_list))
    # # print(res)
    # return(" ".join(res))
          
      


    # print(len(sss))
    
    
 

       
    # ss=math.floor(math.sqrt(L))<=row<=colum<=math.ceil(math.sqrt(L))
    # print(row)
    # print(colum)

    
   

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
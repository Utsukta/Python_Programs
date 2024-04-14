import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x2>x1:
        if v2>v1:
            return "NO"
    if ((x1-x2) % (v2-v1)==0) and ((x1-x2)//(v2-v1))>0:
        return "Yes"
    else:
        return "No"
    

    # while True:
    #     x1,v1=x1+v1,v1
    #     first_kangaroo.append(x1)
    #     x2,v2=x2+v2,v2
    #     second_kangaroo.append(x2)
    #     for i in range(data_len):
    #         if first_kangaroo[i]==second_kangaroo[i]:
    #              print("yes")
    #              break
            
    #         else:
    #             print("no")
    #             break
        
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def LCMofArray(a):
  lcm = a[0]
  for i in range(1, len(a)):
    lcm = lcm * a[i] // math.gcd(lcm, a[i])
  return lcm


def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    
    lcm = LCMofArray(a)
    print(lcm)

    lst1 = [i for i in range(lcm, min(b) + 1) for num in a if i % num == 0]
    lst = []
    for i in range(lcm, min(b) + 1):
        fl = True
        for num in a:
            if i % num != 0 : 
                fl = False
                break
        if fl: lst.append(i)
           
    print(lst)
    print(lst1)
    cnt = 0
    for num in lst:
        fl = True
        for val in b:
            if val % num != 0: 
                fl = False
                break
        if fl :
            print(num) 
            cnt += 1    
    
    return cnt  


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')
    print(total)

    # fptr.close()

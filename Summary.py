
#!/bin/python3

import math
import os
import random
import re
import sys
from operator import truediv

from django.db.models.functions import TruncYear


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertion_sort(l):
    # Write your code here
    cnt = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           cnt += 1
           j -= 1
        l[j+1] = key
        #cnt += 1

    return cnt

if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))


    n = 2
    arr = [2, 1]

    n = 7
    arr = [3, 4, 7, 5, 6, 2, 1]

    n = 6
    ar = [2, 1, 3, 1, 2]

    print(insertion_sort(ar))
    print(" ".join(map(str, ar)))

----------------------------

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import truediv

from django.db.models.functions import TruncYear


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    # Write your code here
    condition = True
    l = n
    t = arr[n-1]
    if n == 1:
        print(' '.join(map(str, arr)))
        return
    for j in range(1,l):
        i = j
        t = arr[j]
        condition = True
        while condition:
            if t < arr[i-1] and i > 0:
                arr[i] = arr[i-1]
                i -= 1
            else:
                arr[i] = t
                condition = False
        print(' '.join(map(str,arr)))

if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))


    n = 2
    arr = [2, 1]

    n = 7
    arr = [3, 4, 7, 5, 6, 2, 1]

    n = 6
    arr = [1, 4, 3, 5, 6, 2]
    insertionSort2(n, arr)

-----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

from django.db.models.functions import TruncYear


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    l = True
    i = n - 1
    t = arr[n-1]
    if n == 1:
        print(' '.join(map(str, arr)))
        return

    while l:
        if t < arr[i-1] and i > 0:
            arr[i] = arr[i-1]
            i -= 1
        else:
            arr[i] = t
            l = False
        print(' '.join(map(str,arr)))


if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))
    n = 5
    arr = [2, 4, 6, 8, 3]

    n = 2
    arr = [2, 1]

    insertionSort1(n, arr)

--------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    # Write your code here
    lengths = {len(i) for i in unsorted}
    print(type(lengths))
    s = []
    for l in sorted(list(lengths)):
        t = filter(lambda x: len(x) == l, unsorted)
        s += sorted(t)
    return s

if __name__ == '__main__':

    unsorted = ['8',
                '1',
                '2',
                '100',
                '12303479849857341718340192371',
                '3084193741082937',
                '3084193741082938',
                '111',
                '200',
                '443',
                '122']

    my_file = open("idata.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    unsorted = data.split("\n")
    my_file.close()
    result = bigSorting(unsorted)
    print(len(unsorted))
    print('\n'.join(result))
    
-----------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    ref = 3
    n = t
    while True:
        #print(n)
        if n <= ref:
            return(ref - n + 1)
        n = t - ref
        ref = 2 * ref
        t = n

if __name__ == '__main__':
    for i in range(1, 25):
        result = strangeCounter(i)
        print(i, result)

-----------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    #print(b)
    ladybugs = list(set([string for string in b if string != "_"]))
    if "_" not in b:
        for d in ladybugs:
            #print(b.count(d))
            if(b.count(d)==1):
                return "NO"
        for bug in range(1, len(b) - 1):
            if b[bug] == b[bug - 1] or b[bug] == b[bug + 1]:
                continue
            else:
                return "NO"
        return "YES"
    else:
        for d in ladybugs:
            #print(b.count(d))
            if(b.count(d)==1):
                return "NO"
        return "YES"

if __name__ == '__main__':

    b = []
    b.append("AABBC")
    b.append("AABBC_C")
    b.append("__")
    b.append("DD__FQ_QQF")
    b.append("AABCBC")
    for bd in b:
        result = happyLadybugs(bd)
        print(result)

-----------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
        for i in range(len(G) - len(P) + 1):
                if P[0] not in G[i]:
                        continue

                for j in range(len(G[0]) - len(P[0]) + 1):
                        if P[0] != G[i][j:j + len(P[0])]:
                                continue

                        for k in range(1, len(P)):
                                if P[k] != G[i + k][j:j + len(P[0])]:
                                        break

                                if k == len(P) - 1:
                                        return "YES"

        return "NO"

if __name__ == '__main__':
    G=['7283455864','6731158619','8988242643','3839515324','9509509509','5633845374','6473530293','7053106601','0834282956','4607924137']
    P = ["9509","3845","3530"]
    result = gridSearch(G, P)
    print(result)

-------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations_with_replacement, permutations, product

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    finals = []
    for first in range(n):
        finals.append(first * max(a, b) + (n - first - 1) * min(a, b))
    return sorted(list(set(finals)))

if __name__ == '__main__':

    T = 1

    for T_itr in range(T):
        n = 1000

        a = 999

        b = 1000

        result = stones(n, a, b)
        print(result)

------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def isMagic(s):
    for i in range(3):
        if sum(s[i*3:i*3+3]) != 15:
            return False
        if sum(s[i::3]) != 15:
            return False
    if s[0] + s[4] + s[8] != 15:
        return False
    if s[2] + s[4] + s[6] != 15:
        return False
    return True

def formingMagicSquare(s):
    # Write your code here
    ref=[i for j in s for i in j]
    min_cost = 1000
    best = None
    for p in permutations(range(1, 10)):
        cost = sum([abs(p[i] - ref[i]) for i in range(len(ref))])
        if cost < min_cost and isMagic(p):
            min_cost = cost
            best = p

    return(min_cost)

if __name__ == '__main__':

    s = []
    s.append([5, 3, 4])
    s.append([1, 5, 8])
    s.append([6, 4, 2])

    result = formingMagicSquare(s)

    print(result)

-------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    cavity = []
    for i in range(1,len(grid) - 1):
        for j in range(1,len(grid[i])-1):
            r = []
            #print(int(grid[i][j]))
            r.append(int(grid[i][j])-int(grid[i+1][j]))
            r.append(int(grid[i][j])-int(grid[i-1][j]))
            r.append(int(grid[i][j])-int(grid[i][j-1]))
            r.append(int(grid[i][j])-int(grid[i][j+1]))
            if min(r) > 0:
                cavity.append(list(map(int,(i, j))))
    for i in range(0,len(cavity)):
        #print(cavity[i][0],cavity[i][1])
        t = list(grid[cavity[i][0]])
        #print(t)
        t[cavity[i][1]] = 'X'
        #print(''.join(t))
        grid[cavity[i][0]] = ''.join(t)
    #print(cavity)
    return grid

if __name__ == '__main__':

    n = 4
    grid = ['1112', '1912', '1892', '1234']
    result = cavityMap(grid)

    print('\n'.join(result))

----------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    if len(B) > 1:
        t = [i % 2 for i in B].count(1)
        if (t % 2 == 1):
            return 'NO'
        elif (t == 0):
            return '0'
        else:
            indices = [i for i, x in enumerate([i % 2 for i in B]) if x == 1]
            print(indices)
            b = 0
            j = 0
            for i in range(0, len(indices)//2 + len(indices) % 2):
                print(indices[j], indices[j+1])
                b += indices[j+1] - indices[j]
                j = i * 2 + 2
            #print([(indices[i], indices[i+1]) for i in range(len(indices) - 1)])
            #return (str)(sum(list(map(lambda x, y: y - x, indices[:-1], indices[1:]))) * 2)
            if b == 0: return 'NO'
            return (str) (b * 2)
    else:
        return 'NO'
    #return B


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #N = int(input().strip())
    N = 5

    #B = list(map(int, input().rstrip().split()))
    print(fairRations([10, 1]))
    print(fairRations([2, 2]))
    print(fairRations([2, 3, 4]))
    print(fairRations([2, 3, 3]))
    print(fairRations([1, 1, 1, 1]))
    print(fairRations([1, 1, 1, 1, 10]))
    print(fairRations([2, 3, 4, 5, 6, 7]))
    print(fairRations([2, 3, 4, 5, 6, 8]))
    print(fairRations([1, 4, 4, 4, 6, 5]))
    print(fairRations([3, 5, 7, 9, 5]))
    print(fairRations([3, 5, 7, 9, 5, 7]))


    #fptr.write(result + '\n')

    #fptr.close()
------------------------------------------

# !/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


# Complete the flatlandSpaceStations function below. Flatland Space Stations
def flatlandSpaceStations(n, c):
    c.sort()
    h = max(c[0] - 0, n - 1 - c[len(c) - 1])
    r = 0
    if len(c) > 1:
        r = max([c[i] - c[i - 1] - 1 for i in range(1, len(c))])
    if r > 0:
        if h > ((r // 2) + (r % 2)):
            return h
        else:
            return ((r // 2) + (r % 2))
    else:
        return (h)

    '''    d = []
    c.sort()
    N = list(set(list(range(n))) - set(c))
    #d = [min([abs(j - i) for j in c]) for i in N]

    for K in N:
        t = c[min(range(len(c)), key=lambda i: abs(c[i] - K))]
        t=min(enumerate(c),key=lambda x:abs(K-x[1]))
        sorted_list = sorted(c, key=lambda x: abs(K - x))
        print(sorted_list[0])
        d.append(abs(K-t[1]))
        print(abs(K-t[1]))

    print(d)
    if not d: return 0
    return (max(d))

    print(max([min([abs(j-i) for j in c]) for i in N]))

    for i in N:
        t = min([abs(j-i) for j in c])
        #if t > d: d = t
        d.append(t)
    if len(d) > 0:
        return (max(d))
    return(max(d))

    for i in N:
        t = min([abs(j-i) for j in c])
        if t > d: d = t
    d = 0
    N = list(set(list(range(n))) - set(c))

    for i in N:
        t = min([abs(j-i) for j in c])
        if t > d: d = t
    return(d)
'''


if __name__ == '__main__':
    n = 5
    c = [0, 4]
    result = flatlandSpaceStations(n, c)
    print(result)
#        if i not in c:
#            if i == 0:
#                if i - c[0] > d: d = i - c[0]
#            else:
#            print(i)
#            print(([abs(j-i) for j in c]))
#            print(([abs(j - i) for j in c[::-1]]))

------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    i = 0
    sp = 0
    for a in arr:
        p = 0
        for j in range(0, a//k):
            p += k
            i += 1
            if i > (j*k) and i <= p:
                sp += 1
            #print(p, sp)
        if (a - (a//k * k)) > 0:
            p += a - (a//k * k)
            i += 1
            if i > ((a//k)*k) and i <= p:
                sp += 1
            #print(p, sp)

    return sp
if __name__ == '__main__':
    n = 5
    k = 3
    arr = [4, 2, 6, 1, 10]
    print(workbook(n, k, arr))

--------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#


def serviceLane(n, cases):
    # Write your code here
    result = []
    print("here")
    for a in cases:
        print (width[a[0]:a[1]+1])
        result.append(min(width[a[0]:a[1]+1]))
    return result

if __name__ == '__main__':

    n = 5
    t = 5
    width = [1, 2, 2, 2, 1]
    cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]
    print(serviceLane(n, cases))
    list = ['d', 'e', 'f', 'g']
    print(list[1:3])

---------------------------------------------------

def generate_descending_sequence(start, percentage, num_terms):
    sequence = [start]
    for _ in range(1, num_terms):
        next_value = sequence[-1] * (1 - percentage / 100)
        sequence.append(next_value)
    return sequence

# Example usage
start_number = float(input("Enter the starting number: "))
percentage_decrement = float(input("Enter the percentage decrement: "))
number_of_terms = int(input("Enter the number of terms: "))

sequence = generate_descending_sequence(start_number, percentage_decrement, number_of_terms)

print("Generated descending sequence:")
for num in sequence:
    print(num)

---------------------------------------------------------

#collections.OrderedDict
from collections import OrderedDict

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    od = OrderedDict()
    n = int(input())
    for i in range(0,n):
        item = list(input().split())
        key = " ".join(item[:-1])
        if key not in od.keys():
            val = int(item[-1:][0])
        else:
            val = int(item[-1:][0]) + od[key]
        od.update({key:val})
        #od[" ".join(item[:-1])] = item[-1:][0]
    litems = list(od.keys())
    for k in od.keys():
        print(k, od[k])

_________________________________________________________

#collections.namedtuple()
from collections import namedtuple
#from decimal import *

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    clist = list(input().split())
    Student = namedtuple('Student', clist)
    som = 0
    for i in range(0,n):
        t = list(input().split())
        s = Student(t[0],t[1],t[2],t[3])
        som += int(s.MARKS)
    print("%.2f" % (som/n))

_________________________________________________

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = list(map(int, input().split()))
    A = []
    B = []
    r = {}

    for t_itr in range(t[0]):
        A.append(input().rstrip().split())

    for t_itr in range(t[1]):
        B.append(input().rstrip().split())

    for i in B:
        my_list = []
        for ic in range(len(A)):
            if i == A[ic]:
                my_list.append(ic+1)
        if len(my_list) == 0:
            my_list.append(-1)

        r[str(i)] = my_list

    for i in B:
        print(*r[str(i)])

______________________________________________________________________

def chocolateFeast(n, c, m):
    # Write your code here
    tc = 0
    l = n // c
    tc = l
    while l >= m:
        tc += l // m
        l = l // m + l % m

    return (tc)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

 #       fptr.write(str(result) + '\n')
        print(str(result))

#    fptr.close()

_________________________________________________________


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "one"]
two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def getnum(num):

    result =  ""
    if num <= 10:
        result = single_digits[num]
    elif num < 20:
        result = two_digits[num%10 + 1]
    else:
        result = tens_multiple[int(num/10)]
        if num%10 != 0:
            result += " "
        result += single_digits[num%10]

    return result

def timeInWords(h, m):
    # Write your code here
    result = ""
    if m == 0:
        result = single_digits[h] + " o' clock"
    elif m == 30:
        result = "half past " + single_digits[h]
    elif m % 15 == 0:
        if m / 15 == 1:
            result = "quarter past " + single_digits[h]
        else:
            result = "quarter to " + single_digits[h+1]
    elif m > 30:
        result = getnum(60-m)
        if 60-m == 1:
            result += " minute to "
        else:
            result += " minutes to "
        result += single_digits[h+1]
    else:
        result = getnum(m)
        if m == 1:
            result += " minute past "
        else:
            result += " minutes past "
        result += single_digits[h]
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    for i in range(0,60):
        result = timeInWords(1, i)
        print (result)

    #fptr.write(result + '\n')

    #fptr.close()

_________________________________________________________
#Introduction to Sets
def average(array):
    # your code goes here
    l = []
    k = [l.append(i) for i in array if i not in l]
    number = round(float(sum(l)) / float(len(l)), 3)
    return number

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
______________________________________________

#Polar Coordinates
from cmath import phase

if __name__ == '__main__':
    compnum = input()
    print(abs(complex(compnum)))
    print(phase(complex(compnum)))

______________________________________________

#itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

if __name__ == '__main__':
    word, num = input().split(" ")
    print(*[''.join(j) for j in combinations_with_replacement(sorted(word), int(num))], sep='\n')

______________________________________________

# itertools.combinations()
from itertools import combinations

if __name__ == '__main__':
    word, num = input().split(" ")
    print(*[''.join(j) for i in range(1, int(num)+1) for j in combinations(sorted(word), i)], sep='\n')

______________________________________________

# itertools.permutations() 
from itertools import permutations
if __name__ == '__main__':
    word, num = input().split(" ")
    permutations = list(permutations(word, int(num)))
    permutations.sort()

    [print("".join(i)) for i in permutations]
______________________________________________

# itertools.permutations() - Manual
# Enter your code here. Read input from STDIN. Print output to STDOUT
answer = []
base = 0

def permutation(string, i, length):
    #print(''.join(string), ''.join(string)[:base], ''.join(string)[-1*base:])
    if ''.join(string)[:base] not in answer:
        answer.append(''.join(string)[:base])
    if ''.join(string)[-1*base:] not in answer:
        answer.append(''.join(string)[-1*base:])

    if i == length:
        return
    else:
        for j in range(i, length):
            string[i], string[j] = string[j], string[i]

            # keep increasing i by 1 till it becomes equal to 0
            permutation(string, i + 1, length)
        string[i], string[j] = string[j], string[i]

if __name__ == '__main__':
    s = list(input().split(' '))
    if len(s) == 1:
        base = len(s[0])
    else:
        base = int(s[1])
    s = list(s[0])
    s.sort()
    permutation(s, 0, len(s))
    answer.sort()
    for str in answer:
        print(str)
_______________________________________

#Validating UID

def check_validity(str):
    if len(str) != 10:
        return "Invalid"
    if not str.isalnum():
        return "Invalid"
    if max([str.count(s) for s in str]) >= 2:
        return "Invalid"
    if len(list([int(s) for s in str if s.isdigit()])) < 3:
        return "Invalid"
    if (sum(1 for s in str if s.isupper())) < 2:
        return "Invalid"
    return "Valid"

if __name__ == '__main__':
    N = int(input())
    uid = []
    for i in range(N):
        uid.append(input())
    for id in uid:
        print(check_validity(id))

#--------------------------------------------

# List
if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        s = list(input().split(' '))
        cmd = s[0]
        args = s[1:]

        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("ls."+cmd)
        else:
            print(ls)

#------------------------------------

n = 2
x = 1
y = 1
z = 1
matrix = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if (i + j + k) != n]
print(matrix)

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

av = sum(student_marks[query_name]) / len(student_marks[query_name])

print("{:.2f}".format(av))

#----------------------------------------

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(all([a >= 0 for a in arr]) and any(str(num) == str(num)[::-1] for num in arr))

#----------------------------------------

import re
st = str(input().rstrip().split())
l = re.findall("[a-z]", st)
L = re.findall("[A-Z]", st)
n = list(map(int, re.findall("[0-9]", st)))
n.sort()
nbr = ''.join([str(num) for num in n if num % 2 == 1])
nbr += ''.join([str(num) for num in n if num % 2 == 0]) 

l = list(l)
L = list(L)
l.sort()
L.sort()

l = ''.join(l)
L = ''.join(L)

print(l + L + nbr)

#----------------------------------------


def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:i + len(sub_string)] == sub_string : count += 1
        # print(string[i:i + len(sub_string)])        
    
    return count


string = "ABCDCDC"
sub_string = "CDC"

print(count_substring(string, sub_string))

#----------------------------------------

s = "22"

if len([True for str in list(s) if str.isalpha()]) > 0 : print(True)
else: print(False)

#----------------------------------------
# Designer Door Mat
n = 11
m = n * 3
pat = ".|."

p = ""
dl = 1
for i in range(1, (n // 2) + 1):
    print((pat * dl).center(m, '-'))
    dl += 2
print("WELCOME".center(m, '-'))
dl -= 2
for i in range((n // 2) + 1, 1, -1):
    print((pat * dl).center(m, '-'))
    dl -= 2

#----------------------------------------


def print_formatted(number):
    # your code goes here
    pad = len(str(bin(number))[2:])

    for i in range(1, number + 1):
        s = str(i).rjust(pad, ' ') + ' ' + str(oct(i))[2:].rjust(pad, ' ') + ' ' + str(hex(i))[2:].upper().rjust(pad, ' ') + ' ' + str(bin(i))[2:].rjust(pad, ' ')
        print(s)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#----------------------------------------

n = 10
l = n + (n - 1) + (n + (n - 1) - 1)
h = (n * 2) - 1
asc = ord('a') + n - 1
lst = []

for i in range(0, n):
    s = ""
    il = i * 2 + 1
    
    if il == 1: s += chr(asc)
    else:            
        c = asc
        # print(int(il / 2))
        for j in range(0, int(il / 2)):       
            if s == "": s += chr(c)
            else: s += "-" + chr(c)
            c -= 1
            # print(chr(c))
        # c -= int(il / 2)    
        # print(chr(c))    
        s += "-" + chr(c) 
        # c += 1
        for j in range(0, int(il / 2)):
            c += 1
            s += "-" + chr(c)
            # print(chr(c))
    lst.append(s)
    
ln = len(lst) - 2
for i in range(ln, -1, -1):
    lst.append(lst[i])

for s in lst:
    print(s.center(l, '-'))

#----------------------------------------

s = "12abc"
s = s.lower().split()
for i in range(0, len(s)):
    s[i] = list(s[i].strip())

for i in range(0, len(s)):
    s[i][0] = s[i][0].upper()

for i in range(0, len(s)):
    s[i] = ''.join(s[i])

print(' '.join(s))

#----------------------------------------


def minion_game(string):
    # your code goes here
    s = string.strip().upper()
    stuart = {}
    kevin = {}
    v = list("AEIOU")

    for i in range(0, len(s)):        
        for j in range(i + 1, len(s) + 1):
            if s[i] in v:
                if s[i:j] not in kevin.keys(): kevin[s[i:j]] = 1
                else: kevin[s[i:j]] += 1
            else:
                if s[i:j] not in stuart.keys(): stuart[s[i:j]] = 1
                else: stuart[s[i:j]] += 1

    if sum(stuart.values()) > sum(kevin.values()):
        print("Stuart", sum(stuart.values()))
    elif sum(stuart.values()) == sum(kevin.values()):
        print("Draw")
    else:
        print("Kevin", sum(kevin.values()))


if __name__ == '__main__':
    s = input()
    minion_game(s)


#----------------------------------------
def minion_game(string):
    # your code goes here
    s = string.strip().upper()
    n = len(s)
    v = list("AEIOU")
    stuart = 0
    kevin = 0
            
    lst = [s[i:(j + 1)] for i in range(0, n) for j in range(i, n)]
    # print(lst)
    
    for i in range(0, len(lst)):        
        if lst[i][0] in v: kevin += 1
        else: stuart += 1

    if stuart > kevin: print("Stuart", stuart)
    elif stuart == kevin: print("Draw")
    else: print("Kevin", kevin)


s = "amount"
minion_game(s)


#----------------------------------------
def minion_game(string):
    # your code goes here
    vowels = list('AEIOU')
    S = 0
    K = 0
    for i in range(len(string)):
        # print(string[i])
        if string[i] in vowels:
            K += len(string) - i
        else:
            S += len(string) - i
    if S > K:
        print("Stuart" + " " + "%d" % S)
    elif K > S:
        print("Kevin" + " " + '%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


#----------------------------------------
# sWAP cASE
def swap_case(s):    
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#----------------------------------------
# String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line


#----------------------------------------
# What's Your Name?
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#----------------------------------------
# Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#----------------------------------------
# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:i + len(sub_string)] == sub_string : count += 1    
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#----------------------------------------
# String Validators
if __name__ == '__main__':
    s = input()

    if len([True for str in list(s) if str.isalnum()]) > 0 : print(True)
    else: print(False) 

    if len([True for str in list(s) if str.isalpha()]) > 0 : print(True)
    else: print(False)  

    if len([True for str in list(s) if str.isdigit()]) > 0 : print(True)
    else: print(False)  

    if len([True for str in list(s) if str.islower()]) > 0 : print(True)
    else: print(False)  

    if len([True for str in list(s) if str.isupper()]) > 0 : print(True)
    else: print(False)
#----------------------------------------
# Replace all ______ with rjust, ljust or center. 
# Text Alignment

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))    

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))    

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
#----------------------------------------
# Text Wrap
import textwrap


def wrap(string, max_width):
    i = 0
    s = ""

    for i in range(0, len(string), max_width):
        if s != "": s += "\n"
        s += string[i: i + max_width] 
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#----------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Designer Door Mat
arr = list(map(int, input().rstrip().split()))
n = arr[0]
m = arr[1]
pat = ".|."

p = ""
dl = 1
for i in range(1, (n // 2) + 1):
    print((pat * dl).center(m, '-'))
    dl += 2
print("WELCOME".center(m, '-'))
dl -= 2
for i in range((n // 2) + 1, 1, -1):
    print((pat * dl).center(m, '-'))
    dl -= 2


#----------------------------------------
# String Formatting
def print_formatted(number):
    # your code goes here
    pad = len(str(bin(number))[2:])

    for i in range(1, number + 1):
        s = str(i).rjust(pad, ' ') + ' ' + str(oct(i))[2:].rjust(pad, ' ') + ' ' + str(hex(i))[2:].upper().rjust(pad, ' ') + ' ' + str(bin(i))[2:].rjust(pad, ' ')
        print(s)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#----------------------------------------
# Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    n = size
    l = n + (n - 1) + (n + (n - 1) - 1)
    h = (n * 2) - 1
    asc = ord('a') + n - 1
    lst = []

    for i in range(0, n):
        s = ""
        il = i * 2 + 1
        
        if il == 1: s += chr(asc)
        else:            
            c = asc
            # print(int(il / 2))
            for j in range(0, int(il / 2)):       
                if s == "": s += chr(c)
                else: s += "-" + chr(c)
                c -= 1
                # print(chr(c))
            # c -= int(il / 2)    
            # print(chr(c))    
            s += "-" + chr(c) 
            # c += 1
            for j in range(0, int(il / 2)):
                c += 1
                s += "-" + chr(c)
                # print(chr(c))
        lst.append(s)
        
    ln = len(lst) - 2
    for i in range(ln, -1, -1):
        lst.append(lst[i])

    for s in lst:
        print(s.center(l, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#----------------------------------------
# Capitalize
s = "chris alan"
print(' '.join(word.capitalize() for word in s.split(' ')))


#----------------------------------------
# The Minion Game
def minion_game(string):
    # your code goes here
    s = string.strip().upper()
    n = len(s)
    v = list("AEIOU")
    stuart = 0
    kevin = 0
            
    lst = [s[i:(j + 1)] for i in range(0, n) for j in range(i, n)]
    # print(lst)
    
    for i in range(0, len(lst)):        
        if lst[i][0] in v: kevin += 1
        else: stuart += 1

    if stuart > kevin: print("Stuart", stuart)
    elif stuart == kevin: print("Draw")
    else: print("Kevin", kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)


# 2
def minion_game(string):
    # your code goes here
    vowels = list('AEIOU')
    S = 0
    K = 0
    for i in range(len(string)):
        # print(string[i])
        if string[i] in vowels:
            K += len(string) - i
        else:
            S += len(string) - i
    if S > K:
        print("Stuart" + " " + "%d" % S)
    elif K > S:
        print("Kevin" + " " + '%d' % K)
    else:
        print("Draw")


s = "BANANA"
minion_game(s)

    
#----------------------------------------
# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    lst = []
    for i in range(0, len(string), k):
        lst.append(string[i:i + k])
    
    for s in lst:
        cs = []
        for c in s: 
            if c not in cs: cs.append(c)
        print(''.join(cs))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
#----------------------------------------
lst = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
k = 1

d = {}
for i in lst:
    d[i[k]] = i

lst = list(d.keys())
lst.sort()

for i in lst:
    s = ""
    for j in d[i]:
        if s != "" : s += " " 
        s += str(j)
    print(s)
#----------------------------------------
# Breaking the Records
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    Game = [] 
    Score = [] 
    Minimum = [] 
    Maximum = [] 
    rslt = []
    for i in range(0, len(scores)):
        Game.append(i)
        Score.append(scores[i])
        Minimum.append(min(Score))
        Maximum.append(max(Score))

    rslt.append(len(list(set(Maximum))) - 1)
    rslt.append(len(list(set(Minimum))) - 1)
    return rslt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#----------------------------------------    
#!/bin/python3
# Birthday Chocolate

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    share = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            if (j - i) == m and sum(s[i:j]) == d:
                share += 1
    return share


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
    
#----------------------------------------  
# Divisible Sum Pairs
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    share = 0
    for i in range(0, len(ar)):
        for j in range(0, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                print(ar[i], ar[j])
                share += 1
    return share


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Migratory Birds
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d = {}

    for i in arr:
        if i not in d.keys(): d[i] = 1
        else: d[i] += 1

    return (min([k for k in d.keys() if d[k] == max(d.values())]))    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Day of the Programmer

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    mdays = [31, 29, 31, 30, 31, 30, 31, 31]
    day = 256

    if year in range(1700, 1918):
        if year % 4 == 0: mdays[1] = 29
        else: mdays[1] = 28
    elif year == 1918:
        if year % 4 == 0: mdays[1] = 16
        else: mdays[1] = 15  
    elif year in range(1919, 2701):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) : mdays[1] = 29
        else: mdays[1] = 28
 
    date = str(day - sum(mdays)) + ".09." + str(year)
    return date


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
#----------------------------------------    
# Bon Appétit
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    diff = (b - ((sum(bill) - bill[k]) / 2)) 
    if diff == 0:
        print("Bon Appetit")
    else:
        print(int(diff))

        
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
#----------------------------------------
# Sock Merchant
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mp = 0
    d = {}

    for i in ar:
        if i not in d.keys(): d[i] = 1
        else: d[i] += 1
    for i in d.values():
        mp += int(i / 2)
    return mp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Drawing Book
#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    f = int(p / 2)
    if n % 2 == 0: 
        if p % 2 != 0:
            b = int((n - p) / 2) + 1
        else: b = int((n - p) / 2)
    else: b = int((n - p) / 2)

    if f <= b:
        return f
    else:
        return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Counting Valleys
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    step = 0
    lst = []
    for st in s:
        if st == "U": step += 1
        else: step -= 1
        lst.append(step)
    rslt = 0
    for i in range(1, len(lst)):
        if lst[i] == 0 and lst[i - 1] < 0: rslt += 1
    return rslt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Electronics Shop
#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    lst = []
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                lst.append(k + d)
    if len(lst) != 0:
        return (max(lst))
    else:
        return (-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
#----------------------------------------
# Cats and a Mouse
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    c1 = x
    c2 = y
    c1i = 0
    c2i = 0

    if x < z : c1i = 1
    else: c1i = -1
    if y < z : c2i = 1
    else: c2i = -1

    if x < z and y < z:
        while c1 < z and c2 < z:
            c1 += c1i
            c2 += c2i
            print(c1, c2)
    elif x < z and y > z:
        while c1 < z and c2 > z:
            c1 += c1i
            c2 += c2i
            print(c1, c2)
    elif x > z and y < z:
        while c1 > z and c2 < z:
            c1 += c1i
            c2 += c2i
            print(c1, c2)
    elif x > z and y > z:
        while c1 > z and c2 > z:
            c1 += c1i
            c2 += c2i
            print(c1, c2)
            
    if c1 == c2:
        return "Mouse C"
    elif c1 == z:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
#----------------------------------------
# Forming a Magic Square
s = []
s.append(list(map(int, "5 3 4".split())))
s.append(list(map(int, "1 5 8".split())))
s.append(list(map(int, "6 4 2".split())))

print(s)

for l in s:
    print(sum(l))

for i in range(0, len(s[0])):
    sum = 0
    for j in range(0, len(s)):
        sum += s[j][i]
    print(sum)
#----------------------------------------
# Picking Numbers
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    maximum = 0
    for i in a:
        c = a.count(i)
        d = a.count(i - 1)
        c = c + d
        if c > maximum:
            maximum = c
    return (maximum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------------
# Climbing the Leaderboard
scores = list(map(int, "100 100 50 40 40 20 10".split()))
alice = list(map(int, "5 25 50 120".split())) 

lst = []

for a in alice:
    i = 1
    cnt = 1
    while  i < len(scores) and a < scores[i - 1] :
        if scores[i - 1] != scores[i]:
            cnt += 1
        i += 1    
    if a < min(scores): cnt += 1
    lst.append(cnt)
#----------------------------------------
# Climbing the Leaderboard
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort()
    scores.reverse()
    lst = []
    l = len(scores)

    for a in alice:
        while (l > 0) and (a >= scores[l - 1]):
            l -= 1
        lst.append (l + 1)

    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#----------------------------------------
# The Hurdle Race
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hurdleRace function below.
def hurdleRace(k, height):
    potion = max(height) - k

    if potion <= 0: return 0
    else: return potion


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------------
# Designer PDF Viewer
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    i = ord('a')
    return (max([h[ord(w) - i] for w in word]) * len(word))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------------
# Utopian Tree
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n):
    g = 1
    for i in range(1, n + 1):
        if i % 2 == 0: g += 1
        else: g *= 2
    return g


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#---------------------------------
# Angry Professor
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    if len([i for i in a if i <= 0]) < k: return 'YES'
    else: return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
#--------------------------------------------
# Beautiful Days at the Movies
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    return len([n for n in range(i, j + 1) if (n - int(str(n)[::-1])) % k == 0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#---------------------------------------------
# Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for i in range(1, n + 1):
        liked = shared // 2
        shared = liked * 3
        cumulative += liked
        
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
#------------------------------------
# Save the Prisoner
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return (m % n + s - 1) % n or n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------------!
# Circular Array Rotation
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    n = (k % len(a)) 
    a = (a[-n:] + a[:-n]) 
    return ([a[i] for i in queries])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#---------------------------------------------
# Sequence Equation
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the permutationEquation function below.
def permutationEquation(p):
    return [p.index(p.index(i) + 1) + 1 for i in range(1, len(p) + 1)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#-------------------------------------------
# Jumping on the Clouds: Revisited
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 1
    j = 0
    e = 100
    while (j) != 1:
    # for n in range(0, 8):
        j = (i + k) % len(c)
        if c[j - 1] == 1: e -= 3
        else: e -= 1
        i += k
    return (e)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#--------------------------------------------
# Find Digits
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    c = 0
    d = [int(i) for i in str(n) if i != '0']

    for i in d:
        if n % i == 0: c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#------------------------
# Extra Long Factorials
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    print(f)

    
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
#-------------------------------
# Append and Delete
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    c = [s[i:j] for i in range(0, len(s)) for j in range(i + 1, len(s) + 1) if t.count(s[i:j]) > 0 ]
    c = [s[0:j] for j in range(1, len(s) + 1) if t.count(s[0:j]) > 0 ]
    l = 0
    f = False
    tl = len(s) + len(t)

    if len(c) > 0 and s == t:
        l = 2 * len(s)
        if k > tl:
            if tl - l <= k : f = True
        else:
            if tl - l <= k and (k - (tl - l)) % 2 == 0 : f = True        
    elif len(c) > 0 and s[0] == t[0]:
        c = [i for i in c if len(i) == max([len(i) for i in c])][0]
        l = 2 * len(c)
        if tl - l <= k and (k - (tl - l)) % 2 == 0 : f = True
        if tl - l <= k and (k - (tl - l)) > 2 * len(s) : f = True
        if len(t) == len(c):    
            if  tl - l <= k and (k - (tl - l)) > 2 * len(c) : f = True 
    else:
        if k > tl:
            if tl - l <= k: f = True
        else:
            if tl - l <= k and (k - (tl - l)) % 2 == 0 : f = True

    if f:
        return ("Yes")
    else:
        return ("No")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
#---------------------------
# Sherlock and Squares
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):
    s = 0
    c = 0
    for n in range(a, b + 1):
        if (n ** 0.5 == int(n ** 0.5)): 
            s = n
            break

    if s != 0:
        s = int(s ** 0.5)
        while s * s <= b:
            s += 1
            c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
#-----------------------------
# Library Fine
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    fee = 0
    if y1 < y2:
        fee = 0
    elif y1 - y2 > 0:
        fee = 10000
    elif m1 < m2 :
        fee = 0
    elif m1 - m2 > 0:
        fee = 500 * (m1 - m2)
    elif d1 < d2 :
        fee = 0
    elif d1 - d2 > 0 :
        fee = 15 * (d1 - d2)
    return fee


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
#--------------------------------
# Cut the sticks
#!/bin/python3

import math
import os
import random
import re
import sys
global rslt


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    global rslt
    # print(len([n for n in arr if n != 0]))
    rslt.append(len([n for n in arr if n != 0]))
    arr = [n - min(arr) for n in arr]
    if len([n for n in arr if n != 0]) == 0:
        return rslt
    else:
        cutTheSticks([n for n in arr if n != 0]) 
        return rslt 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rslt = []
    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#--------------------------------
# Non-Divisible Subset
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    t = [x % k for x in s]
    c = 0
    for i in range(0, len(t)):
        lst = []
        lst.append(t[i])
        for j in range(0, len(t)):
            if i != j:
                if len([x for x in lst if x + t[j] == k]) == 0: 
                    if t[j] == 0 :
                        if lst.count(0) == 0: lst.append(t[j])
                    else:
                        lst.append(t[j])
        if len(lst) > c: c = len(lst)    

    return (c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#2-------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    d = {x:[] for x in range(k)}
    for i in range(len(s)): d[s[i] % k].append(s[i])
    count = 0
    if len(d[0]) > 0:
        count = 1
    S = set([(x, k - x) for x in range(1, k // 2 + 1)])
    for i, j in S:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------------------
# Repeated String
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    ac = s.count('a')
    l = len(s)
    count += ac * (n // l)
    count += s[:n % l].count('a')
    
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
#----------------------------------
# Jumping on the Clouds
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    c.insert(n, 0)
    count = 0
    i = 0 
    while (i < n - 1):
          i += (c[i + 2] == 0) + 1
          count += 1

    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

#------------------------------------------------
# Equalize the Array
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the equalizeArray function below.
def equalizeArray(arr):
    d = {x:arr.count(x) for x in set(arr)}
    return (len(arr) - max(d.values()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#--------------------------------------
# Queen's Attack II
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    c = 0
    d = {x:[1 for y in range(1, n + 1)] for x in range(n, 0, -1) }
    for l in obstacles:
        d[l[0]][l[1] - 1] = 0
    print(d)
    # LT
    print("# LT")
    i = r_q
    for j in range(c_q + 1, n + 1): 
        if d[i][j - 1] == 0: break
        print(i, j)
        c += 1
    for j in range(c_q - 1, 0, -1): 
        if d[i][j - 1] == 0: break
        print(i, j)
        c += 1
    # TB
    print("# TB")
    j = c_q
    for i in range(r_q + 1, n + 1): 
        if d[i][j - 1] == 0: break
        print(i, j)
        c += 1
    for i in range(r_q - 1, 0, -1): 
        if d[i][j - 1] == 0: break
        print(i, j)
        c += 1  
    print(c)
    
    # Forward
    print("# Forward")
    i = r_q
    j = c_q + 1
    for i in range(r_q + 1, n + 1):
        if d[i][j - 1] == 0: break
        print(i, " ", j)        
        j += 1
        c += 1

    i = r_q - 1
    j = c_q - 1
    for j in range(c_q - 1, 0, -1): 
        if d[i][j - 1] == 0: break
        print(i, " ", j)
        i -= 1
        c += 1  
    print(c)    

    # Backward
    print("# Backword")
    i = r_q
    j = c_q - 1
    for i in range(r_q + 1, n + 1):
        if d[i][j - 1] == 0: break
        print(i, " ", j)        
        j -= 1
        c += 1

    i = r_q - 1
    j = c_q - 1
    for j in range(c_q + 1, n + 1): 
        if d[i][j - 1] == 0: break
        print(i, " ", j)
        i -= 1
        c += 1  
    print(c)    
    return(c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
#--------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    u = n - r_q
    d = r_q - 1
    r = n - c_q
    l = c_q - 1
    ru = min(u, r)
    rd = min(r, d)
    lu = min(l, u)
    ld = min(l, d)
    for o in obstacles:
        if o[1] == c_q:
            if o[0] < r_q:
                d = min(d, r_q - 1 - o[0])
            else:
                u = min(u, o[0] - r_q - 1)
        elif o[0] == r_q:
            if o[1] < c_q: l = min(l, c_q - 1 - o[1])
            else: r = min(r, o[1] - c_q - 1)
        elif abs(o[0] - r_q) == abs(o[1] - c_q):
            if o[1] > c_q:
                if o[0] > r_q: ru = min(ru, o[1] - c_q - 1)
                else: rd = min(rd, o[1] - c_q - 1)
            else:
                if o[0] > r_q: lu = min(lu, c_q - 1 - o[1])
                else: ld = min(ld, c_q - 1 - o[1])
                
    return u + d + r + l + ru + rd + lu + ld


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
#---------------------------------------
# ACM ICPC Team
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the acmTeam function below.
def acmTeam(topic):
    d = {i + 1:list(map(int, topic[i])) for i in range(0, len(topic))}
    l = []
    for i in range(1, len(topic) + 1):
        for j in range(i + 1, len(topic) + 1):
            l.append([d[i][x] or d[j][x] for x in range(0, len(d[1]))].count(1))
    return([max(l), l.count(max(l))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#------------------------------------
# Taum and B'day
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#


def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc > wc and bc > wc + z:
        bc = wc + z
    elif wc > bc and wc > bc + z:
        wc = bc + z
    
    cost = b * bc + w * wc 
    return (cost)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
#------------------------------------------------
# Organizing Containers of Balls
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the organizingContainers function below.
def organizingContainers(container):
    
    rowsum = []
    colsum = [0] * len(container)
    
    for r in container:
        rowsum.append(sum(r))
        i = 0
        for c in r:
            # print(i)
            colsum[i] += c
            i += 1

    rowsum.sort()
    colsum.sort()
    
    for i in range(0, len(rowsum)):
        if rowsum[i] != colsum[i]: return "Impossible"
    
    return "Possible" 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
#------------------------------------------------
# Encryption
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")    
    L = len(s)    
    r = math.floor(L ** 0.5)
    c = r + 1
    if r * c < L: r += 1
    rslt = [''] * c
    
    st = [s[i * c:c * (i + 1)] for i in range(0, int(L / c) + 1)]
    
    for ss in st:
        for i in range(0, len(ss)):
            rslt[i] += ss[i]
    
    print(rslt)
    return (' '.join(rslt))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
#---------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")       
    c = math.ceil(len(s) ** 0.5)
    rslt = ""
    for i in range(c):
        rslt += s[i::c] + " "

    return (rslt)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
#---------------------------------------------
# Bigger is Greater
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if w == w[::-1]: return "no answer"
    ar = list(w)
    i = len(ar) - 1
    while i > 0 and ar [i - 1] >= ar[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    j = len(ar) - 1
    while ar[j] <= ar[i - 1]:
        j -= 1
    
    ar[i - 1], ar[j] = ar[j], ar[i - 1]
    ar[i : ] = ar[len(ar) - 1 : i - 1 :-1]
    
    return "".join(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
#-------------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
   for i in range(len(w) - 1)[::-1]:
        for j in range(i + 1, len(w))[::-1]:
            if w[i] < w[j]:
                li = list(w) 
                li[i], li[j] = li[j], li[i]
                return "".join(li[:i + 1] + sorted(li[i + 1:][::-1]))        
   return 'no answer'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
#-------------------------------------------
# Modified Kaprekar Numbers
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    lst = []
    for i in range(p, q + 1):
        l = len(str(i))
        if len(str(i * i)) > 1:
            # print(i, i * i, str(i * i)[:len(str(i * i)) - l], str(i * i)[-(l):])
            if i == int(str(i * i)[:len(str(i * i)) - l]) + int(str(i * i)[-(l):]):
                lst.append(i)            
        else:
            if i == i * i:
                lst.append(i)
    if len(lst) > 0:
        print(' '.join(map(str, lst)))
    else:
        print('INVALID RANGE')

        
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
#-------------------------------------------
# Beautiful Triplets
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    c = []
    c = [[i, j, k] for i in arr for j in arr for k in arr if j - i == d and k - j == d]
    return len(c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    arr.sort(reverse=True)
    cnt = 0
    l = len(arr)
    
    inst = 0
    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] - arr[j] == d:
                for k in range(j + 1, l):
                    if arr[j] - arr[k] == d:
                        # print(arr[i], arr[j])
                        cnt += 1
    return (cnt)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    cnt = 0
    l = len(arr)
    for i in range(l):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            cnt += 1
    return (cnt)    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------
#Minimum Distances
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    cnt = len(a)
#    print(a)
    c = list(set([b for b in a if a.count(b) == 2]))
    if len(c) == 0 : return -1
#    print(c)
    for j in c:
        indx = [index for index, element in enumerate(a) if element ==j]
        diff = indx[1] - indx[0]
#        print(diff)
        if diff < cnt: cnt = diff
    return (cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
#-------------------------------------
#Halloween Sale
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if s < p: return 0
    if s == p: return 1
    cnt = 1
    amt = p
    while p - d > m:
        p = p - d
#        print(p)
        cnt += 1
        amt += p
#    print(amt)
    while amt + m < s:
        amt += m
        cnt += 1
    return (cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
#-------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    cnt = 0
    thr = False
    amt = p
    while int(s/amt) > 0:
        cnt += 1
        if not thr:
            p -= d
        if p < m:
            thr = True
            p = m
        amt += p
    return (cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
#-------------------------------------


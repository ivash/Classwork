#!/usr/bin/python

import sys
import timeit

# A simple memoization function for fib. numbers from 1 - n
# creates an list of size n and computes fib values for each element
# @param int n, size of memoization array
# @return list memo resulting array
def memo_make(n):
    
    memo = []
    for i in range(n+1):
        # insert the fib. number for i 
        # memo list
        memo.append(Fib_normal(i))
    
    return memo

def Fib_memo(x):
    return memo_list[x]


# A simple fibonacci function
# 
# @param x int number of fib squence to be calculated. x must be > 0.
# @return f final result after calc. -1 if invalid is entered
def Fib_normal(x):
    c=1
    n=1
    if(x<=0):
        # invalid input, return -1
        f=-1
        return f
    elif(x<=2):
        # input is 1 or 2, ans = 1
        f=1
        return f
    else:
        for i in (range(x-2) ):
            f = c + n
            c = n
            n = f

    return f

max = 30

memo_list = memo_make(max)

for x in range(1,max+1):
    mytime = timeit.Timer('Fib_normal('+str(x)+')','from __main__ import Fib_normal')
    delta = mytime.timeit(1)

    mytime2 = timeit.Timer('Fib_memo('+str(x)+')','from __main__ import Fib_memo')
    delta2 = mytime2.timeit(1)

    print str(x) +' '+str(delta)+' '+str(delta2)
    
#plot time-of-fib-memo 
filename = "mydata.txt"
FILE = open(filename,'w')

max = 100
memo_list = memo_make(max)

for x in range(1,max+1):
    mytime3 = timeit.Timer('Fib_memo('+str(x)+')','from __main__ import Fib_memo')
    delta3 = mytime3.timeit(1)
    FILE.write(str(x)+' '+str(delta3)+'\n')
    
FILE.close()

    

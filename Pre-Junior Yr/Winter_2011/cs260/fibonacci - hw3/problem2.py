#!/usr/bin/python

import sys
import string

# A simple memoization function for fib. numbers from 1 - n
# creates an list of size n and computes fib values for each element
# @param int n, size of memoization array
# @return list memo resulting array
def fib_memoization(n):
    
    memo = []
    for i in range(n+1):
        # insert the fib. number for i 
        # memo list
        memo.append(simple_fib(i))
    
    return memo



# A simple fibonacci function
# 
# @param x int number of fib squence to be calculated. x must be > 0.
# @return f final result after calc. -1 if invalid is entered
def simple_fib(x):
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

max = 100
# genrate memoization list
memo_list = fib_memoization(max)

# flag to quit program
quit=0

while( not quit):
    x = raw_input("Enter a number to lookup fib. answer for (q quit): ")
    if( x == "q" ):
        quit = 1
    elif( int(x) > max):
        print "Input was greater than expected. Max allowed: " + str(max)
    else:
         print "Fib. answer is = " + str(memo_list[int(x)])



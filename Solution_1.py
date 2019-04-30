'''
Problem 1: If we list all the natural numbers below 10 that are multiples of 3
or 5, we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all
the multiples of 3 or 5 below N.
'''

import time

def problem_1(n):
    return(sum([y for y in range(n) if y%3==0 or y%5==0]))

start_time = time.time()
problem_1(1000)
print("--- %s seconds ---" % (time.time() - start_time))

'''
Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

check = [11, 13, 14, 16, 17, 18, 19, 20]

def scope(start, stop, step, check):
    for a in range(start, stop, step):
        if all(a % checks == 0 for checks in check):
            return a
            
x = scope(2520, 999999999, 2, check)
print(x)

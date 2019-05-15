"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time

def is_pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def solution_9(val):
    for a in range(1, val):
        for b in range(1, val - a):
            c = 1000 - b - a
            if c < b:
                break
            if is_pythagorean_triple(a, b, c):
                print(a * b * c)

if __name__ == "__main__":
    start_time = time.time()
    print(solution_9(1000))
    print("--- %s seconds ---" % (time.time() - start_time))

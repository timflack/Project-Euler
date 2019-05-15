"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# Is a case of using the sieve of Eratosthenes again, rather than hardcode can just import the function ;)

import time
import eulerlib

def solution_10(num):
    answer = sum(eulerlib.prime_numbers.primes(num))
    return str(answer)

if __name__ == "__main__":
    start_time = time.time()
    print(solution_10(1999999))
    print("--- %s seconds ---" % (time.time() - start_time))

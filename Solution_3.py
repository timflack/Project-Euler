'''
Problem 3:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor
of a given number N? e.g. for 10, largest prime factor = 5. For 17, largest
prime factor = 17.
'''

def solution_3(n):
    primefac = None
    div = 2 
    while div * div <= n:
        while n % div == 0:
            primefac = div
            n /= div
        div += 1
    if (n > 1): 
        return n 
    return primefac

start_time = time.time()
solution_3(600851475143)
print("--- %s seconds ---" % (time.time() - start_time))

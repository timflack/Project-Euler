import time

def solution_7(val=None):
    isprime = [False] * 2 + [True] * (val - 1)
    values = []
    for i in range(4, val + 1, 2):
        isprime[i] = False
    for i in range(3, int(val ** 0.5 + 1.5), 2):
        if isprime[i]:
            for n in range(i*i, val + 1, i*2):
                isprime[n] = False
    for i in range(3):
        if isprime[i]:
            values.append(i)
    for i in range(3, val + 1, 2):
        if isprime[i]:
            values.append(i)
    return values[10000]

if __name__ == "__main__":
    start_time = time.time()
    print(solution_7(105000))
    print("--- %s seconds ---" % (time.time() - start_time))

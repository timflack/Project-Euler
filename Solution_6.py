import time

def solution_6(val=None):
    val1 = sum(i**2 for i in range(1, val+1))
    print(val1)
    val2 = (sum(i for i in range(1, val+1)))**2
    print(val2)
    return (val2 - val1)


if __name__ == "__main__":
    start_time = time.time()
    print(solution_6(100))
    print("--- %s seconds ---" % (time.time() - start_time))

'''
Problem 4:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest
palindrome made from the product of two 3-digit numbers.
'''

def solution_4(x, y):
    palindromes = []
    for a in range(x, y):
        for b in range(x, y):
            check = str(a * b)
            if check == check[::-1]:
                palindromes.append(int(check))
    return(max(palindromes))

start_time = time.time()
solution_4(100, 1000)
print("--- %s seconds ---" % (time.time() - start_time))

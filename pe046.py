from math import *

def iscomposite(n):
    if n < 4:
        return False
    if n % 2 == 0:
        return True
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return True
    return False

def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

found = True
i = 7
while found:
    i += 2
    if iscomposite(i):
        found = False
        for j in range(1, int(sqrt(i // 2)) + 1):
            k = i - 2 * j * j
            if isprime(k):
                print(i, "=", k, "+", "2 x", j, "^ 2")
                found = True
                break
print(i)

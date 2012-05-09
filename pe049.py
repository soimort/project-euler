import math

def homo(a, b):
    aa = list(i for i in str(a))
    bb = list(i for i in str(b))
    aa.sort()
    bb.sort()
    return aa == bb

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def genPrimes(n):
    primes = [2]
    for k in range(1, n):
        i = primes[k - 1]
        isPrime = False
        while not isPrime:
            i += 1
            isPrime = True
            for p in primes:
                if p * p > i:
                    break
                if i % p == 0:
                    isPrime = False
                    break
        primes.append(i)
    return primes

p = list(i for i in genPrimes(1500) if i > 999 and i < 10000)

for i in range(0, len(p) - 1):
    for j in range(i + 1, len(p)):
        if homo(p[i], p[j]):
            m = (p[i] + p[j]) // 2
            if homo(p[i], m) and isPrime(m):
                print(p[i], m, p[j])

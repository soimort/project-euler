k = 0
i = 2
primes = []
while i < 2000000:
    primes.append(i)
    k += 1
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
print(sum(primes))

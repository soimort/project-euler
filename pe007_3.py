def prime(n):
    primes = [2]
    for k in range(1, n):
        i = primes[k - 1]
        isPrime = False
        while not isPrime:
            i += 1
            isPrime = True
            for p in primes:
                if i % p == 0:
                    isPrime = False
                    break
        primes.append(i)
    return primes[n - 1]

print(prime(10001))

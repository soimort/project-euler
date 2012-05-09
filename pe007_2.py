def prime(n):
    primes = [2]
    for k in range(1, n):
        i = primes[k - 1]
        isPrime = False
        while not isPrime:
            i += 1
            isPrime = True
            for j in range(0, k):
                if i % primes[j] == 0:
                    isPrime = False
                    break
        primes.append(i)
    return primes[n - 1]

print(prime(10001))

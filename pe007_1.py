def prime(n):
    if n == 1:
        return 2
    else:
        i = prime(n - 1)
        isPrime = False
        while not isPrime:
            i += 1
            isPrime = True
            for j in range(1, n):
                if i % prime(j) == 0:
                    isPrime = False
                    break
        return i

print(prime(10001))

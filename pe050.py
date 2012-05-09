from itertools import count
from math import sqrt

def generate_primes(stop_at = 0):
    primes = []
    for n in count(2):
        if 0 < stop_at < n:
            return
        composite = False
        for p in primes:
            if not n % p:
                composite = True
                break
            elif p ** 2 > n:
                break
        if not composite:
            primes.append(n)
            yield n

objective = 1000000
p = list(generate_primes(objective))
n = 2000
while True:
    s = sum(p[0 : 2 * n + 2])
    if s in p:
        print(s, 2 * n + 2)
        exit(0)
    i = 0
    while s <= objective:
        i += 1
        s = sum(p[i : i + (2 * n + 1)])
        if s in p:
            print(s, 2 * n + 1)
            exit(0)
    n -= 1

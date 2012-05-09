import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False;
    return True;

f = lambda n: n * n + a * n + b
max_n, max_a, max_b = 0, 0, 0
r = 1000
for b in range(-r, r + 1):
    for a in range(-r, r + 1):
        n = 0
        while isPrime(f(n)):
            n += 1
        if max_n < n:
            max_n, max_a, max_b = n, a, b
print(max_a * max_b)

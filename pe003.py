#!/usr/bin/env python3
n = 600851475143
while n % 2 == 0:
    n //= 2
i = 1
while n > 1:
    i += 2
    while n % i == 0:
        n //= i
print(i)

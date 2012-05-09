#!/usr/bin/env python3
def gcd(a, b):
    if a:
        return gcd(b % a, a)
    else:
        return b
lcm = lambda a, b: a * b // gcd(a, b)
m = 1
for i in range(2, 21):
    m = lcm(m, i)
print(m)

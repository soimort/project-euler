#!/usr/bin/env python3
a, b, i, sum = 1, 2, 2, 0
while b <= 4000000:
    if b % 2 == 0:
        sum += b
    a, b, i = b, a + b, i + 1
print(sum)

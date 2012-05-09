#!/usr/bin/env python3
for n in range(999, 99, -1):
    m = int(str(n) + str(n)[::-1])
    for i in range(999, 99, -1):
        if m % i == 0 and len(str(m // i)) == 3:
            print(m)
            exit()


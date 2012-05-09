n = 0
s = 1
while s <= 500:
    n += 1
    t = m = (n + 1) * n // 2
    s = 1
    
    p = 2
    counter = 0
    while t % p == 0:
        counter += 1
        t //= p
    s *= counter + 1
    
    p = 1
    while p * p <= m:
        p += 2
        counter = 0
        while t % p == 0:
            counter += 1
            t //= p
        s *= counter + 1

print(m)

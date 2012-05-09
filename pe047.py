import math

def dpf(n):
    p, i = 0, 2
    if n % i == 0:
        p += 1
    while n > 1 and n % i == 0:
        n //= i
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            p += 1
        while n > 1 and n % i == 0:
            n //= i
        if n == 1:
            break
    if n != 1:
        p += 1
    return p

c = 4
i = cons = 0
while cons < c:
    i += 1
    if dpf(i) == c:
        cons += 1
    else:
        cons = 0
print(i - c + 1)

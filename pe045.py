import math

n = 143
while True:
    n += 1
    h = n * (2 * n - 1)
    temp = math.sqrt(1 + 24 * h)
    if int(temp) == temp and (1 + temp) % 6 == 0:
        temp = math.sqrt(1 + 8 * h)
        if int(temp) == temp and (-1 + temp) % 2 == 0:
            print(n, h)
            break

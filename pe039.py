max_s = max_p = 0
for p in range(1, 1001):
    s = 0
    for a in range(1, p // 2 + 1):
        if (p * p - 2 * p * a) % (2 * p - 2 * a) == 0:
            b = (p * p - 2 * p * a) // (2 * p - 2 * a)
            c = p - a - b;
            if 0 < a <= b:
                s += 1
    if s > max_s:
        max_s, max_p = s, p

print(max_p, max_s)

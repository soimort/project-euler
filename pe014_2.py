max_s = 0
steps = [0]
for i in range(1, 1000001):
    n = i
    s = 0
    while n != 1:
        if n < i:
            s += steps[n]
            break
        s += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    steps.append(s)
    # print(":", i, s)
    if s > max_s:
        max_s = s
        max_i = i
print(max_i, max_s)

def pand(a, b, c):
    m = []
    for i in str(a) + str(b) + str(c):
        if i in m or i == '0':
            return False
        m.append(i)
    if len(m) != 9:
        return False
    return True

p = []
for a in range(1, 10):
    for b in range(1000, 10000):
        c = a * b
        if pand(a, b, c):
            if c not in p:
                p.append(c)
for a in range(10, 100):
    for b in range(100, 1000):
        c = a * b
        if pand(a, b, c):
            if c not in p:
                p.append(c)
print(sum(p))

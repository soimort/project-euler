d, m = 10, 1000000

fac = [1]
for i in range(1, d):
    fac.append(i * fac[i - 1])

def gen(m):
    s = ""
    m -= 1
    for i in range(d - 1, -1, -1):
        t, p = m // fac[i], -1
        m -= fac[i] * t
        while t >= 0:
            p += 1
            if str(p) not in s:
                t -= 1
        s += str(p)
    return s

print(gen(m))

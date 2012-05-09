def d(n):
    temp = 0
    for i in range(1, n):
        if n % i == 0:
            temp += i
    return temp
s = 0
for a in range(1, 10000):
    da = d(a)
    if d(da) == a and da != a:
        s += a
        print(a, d(a))
print(s)

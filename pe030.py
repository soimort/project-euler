m = 0
for i in range(10, 1000000):
    s = str(i)
    t = 0
    for j in range(len(s)):
        t += int(s[j]) ** 5
    if t == i:
        m += i
print(m)

import math
def abundant(n):
    temp = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp += i
            if i != n // i:
                temp += n // i
    return temp > n
m = 28124

a = []
for i in range(1, m):
    if abundant(i):
        a.append(i)

b = [False] * m
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] + a[j] < m:
            b[a[i] + a[j]] = True

print(sum(i for i in range(1, m) if not b[i]))

d = ''
for i in range(1, 1000000):
    d += str(i)
ans, j = 1, 1000000
while j >= 1:
    ans *= int(d[j - 1])
    j //= 10
print(ans)

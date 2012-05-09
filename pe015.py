a = 20
s = [1] * (a + 1)
for i in range(1, a + 1):
    for j in range(1, a + 1):
        s[j] += s[j - 1]
print(s[a])

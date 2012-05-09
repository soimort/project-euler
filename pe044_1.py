p = []
for n in range(1, 3000):
    p.append(n * (3 * n - 1) // 2)

for a in range(0, len(p) - 1):
    for b in range(a + 1, len(p)):
        if p[b] - p[a] in p and p[b] + p[a] in p:
                print(p[b] - p[a])

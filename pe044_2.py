p = {}
for n in range(1, 3000):
    p[str(n * (3 * n - 1) // 2)] = 1

for a in p:
    for b in p:
        if int(a) < int(b) and str(int(b) - int(a)) in p and str(int(b) + int(a)) in p:
            print(int(b) - int(a))

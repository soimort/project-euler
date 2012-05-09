fac = lambda n: int(n == 0) or n * fac(n - 1)
f = []
for i in range(10):
    f.append(fac(i))
print(sum(i for i in range(10, 10000000) if sum(f[int(j)] for j in str(i)) == i))

n = 200
values = [1, 2, 5, 10, 20, 50, 100, 200]
ww = {}
for v in values:
    if v == 1:
        ww[str(v)] = [1] * (n + 1)
    else:
        ww[str(v)] = [1] + [0] * n
        for i in range(1, n + 1):
            ww[str(v)][i] = sum(ww[str(values[values.index(v) - 1])][i - v * j] for j in range(i // v + 1))
print(ww[str(n)][n])

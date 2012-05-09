n = 200
values = [1, 2, 5, 10, 20, 50, 100, 200]
ww = [1] + [0] * n
for i in values:
    for j in range(i, n + 1):
        ww[j] = ww[j] + ww[j - i]
print ww[n]

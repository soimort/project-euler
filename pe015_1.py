f = lambda m, n: int(m == 0) or int(n == 0) or f(m - 1, n) + f(m, n - 1)
print(f(10, 10))

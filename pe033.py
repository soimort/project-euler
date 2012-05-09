n, d = 1, 1
for n2 in range(1, 10):
    for n1 in range(10):
        for d2 in range(1, 10):
            for d1 in range(10):
                if (n2 == d2 and n2 != n1 and d2 != d1 and n1 != d1):
                    if (n2 * 10 + n1) * d1 == (d2 * 10 + d1) * n1 and d1 > n1:
                        n, d = n * n1, d * d1
                if (n2 == d1 and n2 != n1 and d2 != d1 and n1 != d2):
                    if (n2 * 10 + n1) * d2 == (d2 * 10 + d1) * n1 and d2 > n1:
                        n, d = n * n1, d * d2
                if (n1 == d2 and n2 != n1 and d2 != d1 and n2 != d1):
                    if (n2 * 10 + n1) * d1 == (d2 * 10 + d1) * n2 and d1 > n2:
                        n, d = n * n2, d * d1
                if (n1 == d1 and n2 != n1 and d2 != d1 and n2 != d2 and n1 != 0):
                    if (n2 * 10 + n1) * d2 == (d2 * 10 + d1) * n2 and d2 > n2:
                        n, d = n * n2, d * d2
print(n, d)

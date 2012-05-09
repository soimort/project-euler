f, i, l = [0, 1, 1], 2, 1
while l < 1000:
    i += 1
    f.append(f[i - 2] + f[i - 1])
    l = len(str(f[i]))
print(i)

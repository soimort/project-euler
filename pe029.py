s = []
for a in range(2, 101):
    for b in range(2, 101):
        r = a ** b
        if r not in s:
            s.append(r)
print(len(s))

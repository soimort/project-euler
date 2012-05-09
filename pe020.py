s = 1
for i in range(1, 101):
    s *= i
print(sum(int(x) for x in str(s)))

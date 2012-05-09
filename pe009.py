a = 0
while True:
    a += 1
    if 1000 * (500 - a) % (1000 - a) == 0:
        break
b = 1000 * (500 - a) // (1000 - a)
c = 1000 - a - b
print(a * b * c)

max_s = 0

def check(s):
    temp = []
    for c in s:
        if c not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
        elif c in temp:
            return False
        temp.append(c)
    if len(temp) == 9:
        return True
    else:
        return False

for a in range(1, 10):
    for n in range(5, 9):
        s = ''
        for j in range(n):
            s += str(a * (j + 1))
        if check(s):
            max_s = max(max_s, int(s))

for a in range(10, 100):    
    n = 4
    s = ''
    for j in range(n):
        s += str(a * (j + 1))
    if check(s):
        max_s = max(max_s, int(s))

for a in range(100, 1000):
    n = 3
    s = ''
    for j in range(n):
        s += str(a * (j + 1))
    if check(s):
        max_s = max(max_s, int(s))

for a in range(1000, 10000):
    n = 2
    s = ''
    for j in range(n):
        s += str(a * (j + 1))
    if check(s):
        max_s = max(max_s, int(s))

print(max_s)

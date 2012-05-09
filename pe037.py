import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

tp = []
n = 10
for c in range(11):
    while True:
        t = str(n)
        flag = True
        for i in range(1, len(t)):
            if not isPrime(int(t[:i])) or not isPrime(int(t[i:])):
                flag = False
                break
        if flag and not isPrime(n):
            flag = False
        if flag:
            tp.append(n)
            n += 1
            break
        else:
            n += 1
print(sum(tp))

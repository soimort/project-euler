import math

def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def next(s):
    p = len(s) - 1
    while p > 0 and s[p - 1] < s[p]:
        p -= 1
    if p > 0:
        temp = s
        temp[p - 1] -= 1
        while temp[p - 1] in temp[:(p - 1)]:
            temp[p - 1] -= 1
        count = len(s)
        for i in range(p, len(s)):
            while count in temp[:i]:
                count -= 1
            temp[i] = count
        return temp
    else:
        return None

a = [i for i in range(7, 0, -1)]
while a != None:
    s = ''
    for i in a:
        s += str(i)
    if isprime(int(s)):
        print(s)
        break
    a = next(a)

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
s = []
for i in range(1, 1000001):
    flag = True
    for j in range(len(str(i))):
        temp = str(i)[j:] + str(i)[:j]
        if temp in s:
            break
        else:
            if not isPrime(int(temp)):
                flag = False
                break
    if flag:
        s.append(i)
print(len(s))

def bin(n):
    t = ''
    while n > 0:
        t = str(n % 2) + t
        n //= 2
    return t
def isPal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
print(sum(i for i in range(1000000) if isPal(str(i)) and isPal(bin(i))))

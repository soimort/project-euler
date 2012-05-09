import math

def next(s):
    p = len(s) - 1
    while p > 0 and s[p - 1] < s[p]:
        p -= 1
    
    if p > 0:
        temp = s
        temp[p - 1] -= 1
        while temp[p - 1] in temp[:(p - 1)]:
            temp[p - 1] -= 1
        
        count = len(s) - 1
        for i in range(p, len(s)):
            while count in temp[:i]:
                count -= 1
            temp[i] = count
        
        return temp
    else:
        return None

a = [i for i in range(9, -1, -1)]
m = 0
while a != None:
    s = ''
    for i in a:
        s += str(i)
    if int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0 and int(s[3:6]) % 5 == 0 and int(s[4:7]) % 7 == 0 and int(s[5:8]) % 11 == 0 and int(s[6:9]) % 13 == 0 and int(s[7:10]) % 17 == 0:
        m += int(s)
    a = next(a)
print(m)

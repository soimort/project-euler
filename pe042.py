import math

def istriangle(t):
    m = sum(ord(ch) - ord('A') + 1 for ch in t)
    return int(math.sqrt(1 + 8 * m)) ** 2 == 1 + 8 * m

f = open('pe042.in', 'r')
for line in f:
    s = line[1:-1].split("\",\"")
    print(sum(1 for t in s if istriangle(t)))

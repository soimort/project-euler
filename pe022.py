av = lambda str: sum(ord(c) - 64 for c in str)
f = open('pe022.in', 'r')
for line in f:
    m = line.split(",")
s = []
for i in m:
    s.append(i.strip("\""))
s.sort()
ts = 0
for i in range(len(s)):
    ts += (i + 1) * av(s[i])
print(ts)

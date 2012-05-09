f = open('pe013.in', 'r')
m = []
for line in f:
    m.append(int(line))
print(str(sum(m))[:10])

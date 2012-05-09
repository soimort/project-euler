f = open('pe018.in', 'r')
m = []
i = 0
for line in f:
    m.append([])
    for j in line.split(' '):
        m[i].append(int(j))
    i += 1
for i in range(1, len(m)):
    for j in range(len(m[i])):
        if 0 < j < i:
            m[i][j] += max(m[i - 1][j - 1], m[i - 1][j])
        elif j == 0:
            m[i][j] += m[i - 1][j]
        else:
            m[j][j] += m[i - 1][j - 1]
print(max(m[len(m) - 1]))

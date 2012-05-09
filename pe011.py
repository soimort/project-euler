f = open('pe011.in', 'r')
m = []
max_r = 0
for line in f:
    m.append(line.split())
for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j] = int(m[i][j])
for i in range(len(m)):
    for j in range(len(m[0])):
        if j + 3 < len(m[0]):
            temp = m[i][j] * m[i][j + 1] * m[i][j + 2] * m[i][j + 3]
            if temp > max_r:
                max_r = temp
        if i + 3 < len(m):
            temp = m[i][j] * m[i + 1][j] * m[i + 2][j] * m[i + 3][j]
            if temp > max_r:
                max_r = temp
        if i + 3 < len(m) and j + 3 < len(m[0]):
            temp = m[i][j] * m[i + 1][j + 1] * m[i + 2][j + 2] * m[i + 3][j + 3]
            if temp > max_r:
                max_r = temp
        if i - 3 >= 0 and j + 3 < len(m[0]):
            temp = m[i][j] * m[i - 1][j + 1] * m[i - 2][j + 2] * m[i - 3][j + 3]
            if temp > max_r:
                max_r = temp
print(max_r)

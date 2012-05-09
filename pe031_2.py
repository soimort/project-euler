values = [1, 2, 5, 10, 20, 50, 100, 200]
def ww(total, max_value):
    if total == 0:
        return 1
    temp = 0
    for v in values:
        if v <= max_value and total >= v:
            temp += ww(total - v, v)
    return temp
print(ww(200, 200))

values = [1, 2, 5, 10, 20, 50, 100, 200]
def ww(total, max_value):
    if total == 0:
        return 1
    return sum(ww(total - v, v) for v in values if v <= max_value and total >= v)
print(ww(200, 200))

def numOfDays(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
        return 29
    else:
        return 28
s = 1
m = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        s = (s + numOfDays(year, month)) % 7
        if s == 0 and (year > 1900 or (year == 1900 and month == 12)) and not (year == 2000 and month == 12):
            m += 1
print(m)

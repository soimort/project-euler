lrc = lrc_d = 0
for d in range(2, 1000):
    r = 1
    rr = []
    while r != 0:
        while r < d:
            r *= 10
        r %= d
        if r not in rr:
            rr.append(r)
        else:
            break
    if len(rr) > lrc and 0 not in rr:
        lrc, lrc_d = len(rr), d

print(lrc_d)

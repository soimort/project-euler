#!/usr/bin/env python2
sum = 0
for i in range(0, 1000, 3):
    sum += i
for i in range(0, 1000, 5):
    sum += i
for i in range(0, 1000, 15):
    sum -= i
print sum

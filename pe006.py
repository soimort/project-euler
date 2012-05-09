#!/usr/bin/env python3
print(((100 + 1) * 100 // 2) ** 2
    - sum([i ** 2 for i in range(1, 101)]))

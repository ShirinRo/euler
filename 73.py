from fractions import Fraction as fr
import math
import numpy as np

MAX = 12000
sieveOfMisha = np.full((MAX + 1, MAX + 1), True)
print("---")
for d in range(MAX + 1):
    if d % 100:
        print(d)
    for n in range(MAX + 1):
        if n >= d or n == 0 or d == 0:
            sieveOfMisha[d][n] = False
        if not sieveOfMisha[d][n]:
            continue
        mult = 2
        while mult * d < MAX + 1:
            sieveOfMisha[d * mult][n * mult] = False
            mult += 1

c = 0
for d in range(MAX + 1):
    for n in range(math.ceil(d / 3), math.ceil(d / 2)):
        if sieveOfMisha[d][n]:
            print(fr(n, d))
            c += 1

print(c - 1) # because the range includes (1 / 3). lol.
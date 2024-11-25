import math as mt

def choose(n, r):
    return mt.factorial(n) / (mt.factorial(r) * mt.factorial(n-r))

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if choose(n, r) > 1000000:
            count += 1

print(count)
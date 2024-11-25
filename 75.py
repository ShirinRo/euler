import math


def triplet(m, n):
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return sorted([a, b, c])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



maxNum = 1500000
lis = []
for m in range(1, int(math.sqrt(maxNum)) + 1):
    for n in range(1, m):
        if gcd(m, n) == 1 and (m - n) % 2 == 1:
            lis += [triplet(m, n)]


count = [0] * maxNum
for l in lis:
    s = l[0] + l[1] + l[2]
    if s > maxNum:
        continue
    for i in range(s, maxNum, s):
        count[i] += 1

counter = 0
for c in count:
    if c == 1:
        counter += 1
print(counter)
# lis.sort(key=lambda x: x[0])
# print(lis)
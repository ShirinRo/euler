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



maxNum = 10000
lis = []
for m in range(1, int(math.sqrt(maxNum)) + 1):
    for n in range(1, m):
        if gcd(m, n) == 1 and (m - n) % 2 == 1:
            lis += [triplet(m, n)]


perims = [0] * 1001
for tripl in lis:
    original_sum = sum(tripl)
    cur_sum = original_sum
    while cur_sum < 1001:
        if cur_sum == 120:
            print(tripl)
        perims[cur_sum] += 1
        cur_sum += original_sum
m = max(perims)
print(m)
print(perims.index(m))



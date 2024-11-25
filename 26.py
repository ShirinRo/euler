import math
import decimal as decimal


def frac(f):
    return abs(int(f) - f)


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def cycles(n):
    max_k = 1
    max_d = 3
    cc = []
    for s in range(3, n):
        if not is_prime(s) or n % s == 0:
            continue
        num = decimal.Decimal(1 / s)
        k = 1
        while not isclose(frac(num), frac(decimal.Decimal((1 * (10 ** k)) / s))):
            k += 1
        if k > max_k:
            max_k = k
            max_d = s
        cc += [k]
    return max_d
#
# print(cycles(1000))
#

max_k = 1
max_d = 3

def only_nines(n):
    k = 1
    while int('9' * k) % n != 0:
        k += 1

    return k

print(only_nines(3))


for i in range(3, 1000):
    if not is_prime(i) or 1000 % i == 0:
        continue
    i_k = only_nines(i)
    if i_k > max_k:
        max_k = i_k
        max_d = i

print(max_d)
print(max_k)
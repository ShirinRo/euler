import math


def precise_sqrt(n, num_digits):
    digits = []
    a = 0
    while (a + 1) ** 2 <= n:
        a += 1
    digits += [a]
    tmp = n - a ** 2
    while len(digits) < num_digits:
        x = int("".join([str(d) for d in digits]))
        limit = 20 * x
        a = 0
        cand = (limit + a) * a
        tmp = tmp * 100
        while cand <= tmp:
            a += 1
            cand = (limit + a) * a
        a = max(a - 1, 0)
        digits += [a]
        tmp = tmp - (limit + a) * a
    return digits

precise_sqrt_sum = 0

for i in range(1, 101):
    if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
        continue
    precise_sqrt_sum += sum(precise_sqrt(i, 100))

print(precise_sqrt_sum)
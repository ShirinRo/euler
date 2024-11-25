import math

def generalized_pentagonal(k):
    return int(0.5 * k * (3 * k - 1))

def partitions(n, previously_calculated):
    k = 1
    gk = generalized_pentagonal(k)
    n_to_sum = []
    gks = [gk]
    while gk <= n:
        n_to_sum += [int(math.pow(-1, k - 1)) * previously_calculated[n - gk]]
        if k < 0:
            k *= -1
            k += 1
        else:
            k *= -1
        gk = generalized_pentagonal(k)
        gks += [gk]
    return int(sum(n_to_sum))

import numpy as np

previously_calculated = [1, 1]
found_i = 0
i = 2

while found_i == 0:
    pn = partitions(i, previously_calculated)
    previously_calculated += [pn]
    print(f"{i}: {pn}")
    if pn % (10 ** 6) == 0:
        found_i = i
        print(found_i)
    i += 1
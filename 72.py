from fractions import Fraction
from utils import *
import functools


# from exercise 70
def number_of_prime_factors_until_n(n):
    arr = [list() for i in range(n)]
    for i in range(2, n):
        if arr[i] == []:
            for j in range(2 * i, n, i):
                arr[j] += [i]
    return arr

def find_phi_of_n_until_n(n):
    factors = number_of_prime_factors_until_n(n)
    arr = [0] * n
    for i in range(1, n):
        if i % 100 == 0:
            print(i)
        if len(factors[i]) == 0:
            arr[i] = i - 1
        else:
            arr[i] = round(functools.reduce(lambda a, b: a * (1 - 1 / b), [1] + factors[i]) * i)
    return arr

MAX = 10 ** 6
phis = find_phi_of_n_until_n(MAX + 1)
print(sum(phis))

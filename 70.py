from utils import *
import functools

def arePermutations(n, m):
    list_m = list(str(m))
    list_n = list(str(n))
    for digit in set(list_n):
        if list_n.count(digit) != list_m.count(digit):
            return False
    return True


def findPrimeFactors(integer, factors):
    if is_prime(integer):
        factors += [integer]
        return factors
    for i in range(2, math.ceil(math.sqrt(integer))):
        if is_prime(i) and integer % i == 0:
            factors += [i]
    return factors


# stolen from wikipedia "Proof of Euler's product formula"
def phi(n):
    if n == 0:
        return 0
    if (is_prime(n)):
        return n - 1
    factors = findPrimeFactors(n, [])
    result = n
    for factor in set(factors):
        result *= (1 - 1/factor)
    return result

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
            arr[i] = round(functools.reduce(lambda a, b : a * (1 - 1 / b), [1] + factors[i]) * i)
    return arr


MAX = 10 ** 7 + 1
phis = find_phi_of_n_until_n(MAX)
min_ratio = 10
cool_n = 0
for n in range(MAX - 1, 1, -1):
    phi_n = phis[n]
    if arePermutations(n, phi_n):
        if min_ratio > n / phi_n:
            min_ratio = n / phi_n
            cool_n = n
            print(f"n: {cool_n} phi_n: {phi_n} ratio: {min_ratio}")



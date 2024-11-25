import math
from utils import *


MAX = 5 * 10 ** 7

def primes_for_power(n):
    max_p = math.floor(math.pow(MAX, 1 / n)) + 1
    sieve = SieveOfEratosthenes(max_p)
    primes = []
    for i in range(max_p):
        if sieve[i]:
            primes += [i]
    return primes

primes_of_4 = primes_for_power(4)
primes_of_3 = primes_for_power(3)
primes_of_2 = primes_for_power(2)

# print(primes_of_4)
# print(primes_of_3)
# print(primes_of_2)

list = []
for prime4 in primes_of_4:
    fourth = prime4 ** 4
    for prime3 in primes_of_3:
        cube = prime3 ** 3
        if fourth + cube > MAX:
            continue
        for prime2 in primes_of_2:
            square = prime2 ** 2
            if fourth + cube + square <= MAX:
                list += [fourth + cube + square]

list = set(list)
print(list)
print(len(list))
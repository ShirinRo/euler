from utils import *

primes = []
for i in range(1000, 10000):
    if is_prime(i):
        primes += [i]

permutations = []


def is_permutation(num1, num2):
    for i in range(10):
        if str(num1).count(str(i)) != str(num2).count(str(i)):
            return False
    return True


for prime in primes:
    didAdd = False
    for i in range(len(permutations)):
        permutation_group = permutations[i]
        other_prime = permutation_group[0]
        if is_permutation(prime, other_prime):
            permutations[i] = permutation_group + [prime]
            didAdd = True
    if not didAdd:
        permutations += [[prime]]

for permutation_group in permutations:
    if len(permutation_group) < 3:
        continue
    for p in permutation_group:
        if p + 3330 in permutation_group and p + 6660 in permutation_group:
            print(str(p) + str(p + 3330) + str(p + 6660))
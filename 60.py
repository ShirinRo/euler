from utils import *
import numpy as np

def areAllConcatenationsPrime(primes):
    i_1 = 0
    i_2 = 1
    while i_1 < len(primes):
        p_1 = primes[i_1]
        while i_2 < len(primes):
            p_2 = primes[i_2]
            n_1 = int(str(p_1) + str(p_2))
            n_2 = int(str(p_2) + str(p_1))
            if not is_prime(n_1) or not is_prime(n_2):
                return False
            i_2 += 1
        i_1 += 1
        i_2 = i_1 + 1
    return True

MAX = 90009000
MAX_FOR_COUPLES = 9000
allPrimes = []
couplesMat = np.zeros((MAX_FOR_COUPLES + 1, MAX_FOR_COUPLES + 1), dtype=bool)
tripletsMat = np.zeros((MAX_FOR_COUPLES + 1, MAX_FOR_COUPLES + 1, MAX_FOR_COUPLES + 1), dtype=bool)
isPrime = SieveOfEratosthenes(MAX)

cur_min_sum = math.inf
for i in range(MAX_FOR_COUPLES + 1):
    if isPrime[i]:
        allPrimes += [i]

couples = []
i_1 = 0
i_2 = 1
primesInCouple: set = set()
while i_1 < len(allPrimes):
    p_1 = allPrimes[i_1]
    while i_2 < len(allPrimes):
        p_2 = allPrimes[i_2]
        n_1 = int(str(p_1) + str(p_2))
        n_2 = int(str(p_2) + str(p_1))
        if isPrime[n_1] and isPrime[n_2]:
            couplesMat[p_1][p_2] = True
            couplesMat[p_2][p_1] = True
            primesInCouple.add(p_1)
            primesInCouple.add(p_2)
            couples += [[p_1, p_2]]
        i_2 += 1
    i_1 += 1
    i_2 = i_1 + 1

print(couples)
print(len(couples))
print(primesInCouple)
print(len(primesInCouple))

triplets = []
primesInTriplets = set()
c = 0
for couple in couples:
    c += 1
    print("couples: " + str(c / len(couples)))
    for prime in primesInCouple:
        p1 = couple[0]
        p2 = couple[1]
        p1p = couplesMat[p1][prime]
        p2p = couplesMat[p2][prime]
        if p1p and p2p:
            tripletsMat[p1][p2][prime] = True
            tripletsMat[p1][prime][p2] = True
            tripletsMat[p2][p1][prime] = True
            tripletsMat[p2][prime][p1] = True
            tripletsMat[prime][p2][p1] = True
            tripletsMat[prime][p1][p2] = True
            triplets += [[p1, p2, prime]]

primesInTriplets = set([item for sublist in triplets for item in sublist])
print(triplets)
print(len(triplets))
print(primesInTriplets)
print(len(primesInTriplets))
print("~~~~~~~~~ I love Shaul ~~~~~~~~~~~~~~~~")

quartets = []
c = 0
for triplet in triplets:
    c += 1
    print("triplets: " + str(c / len(triplets)))
    for prime in primesInTriplets:
        p1 = triplet[0]
        p2 = triplet[1]
        p3 = triplet[2]
        p1p = couplesMat[p1][prime]
        p2p = couplesMat[p2][prime]
        p3p = couplesMat[p3][prime]
        if p1p and p2p and p3p:
            p12p = tripletsMat[p1][p2][prime]
            p23p = tripletsMat[p2][p3][prime]
            p13p = tripletsMat[p3][p1][prime]
            if p12p and p23p and p13p:
                quartet = [p1, p2, p3, prime]
                quartet.sort()
                quartets += [quartet]

primesInQuartets = set([item for sublist in quartets for item in sublist])
print(quartets)
print(len(quartets))
print(f"primes in quartets: {primesInQuartets}")

c = 0
quintets = []
for quartet in quartets:
    c += 1
    print("quartets: " + str(c / len(quartets)))
    for prime in primesInQuartets:
        p1 = quartet[0]
        p2 = quartet[1]
        p3 = quartet[2]
        p4 = quartet[3]
        p1p = couplesMat[p1][prime]
        p2p = couplesMat[p2][prime]
        p3p = couplesMat[p3][prime]
        p4p = couplesMat[p4][prime]
        if p1p and p2p and p3p and p4p:
            p12p = tripletsMat[p1][p2][prime]
            p13p = tripletsMat[p1][p3][prime]
            p14p = tripletsMat[p1][p4][prime]
            p23p = tripletsMat[p2][p3][prime]
            p24p = tripletsMat[p2][p4][prime]
            p34p = tripletsMat[p3][p4][prime]
            if p12p and p13p and p14p and p23p and p24p and p34p:
                quintet = [p1, p2, p3, p4, prime]
                quintet.sort()
                quintets += [quintet]
print(quintets)
print(len(quintets))

min_s = np.inf
for q in quintets:
    if sum(q) < min_s:
        min_s = sum(q)

print(f"did we? {min_s}")
from utils import *

def allRotations(n):
    rotations = []
    strNum = str(n)
    numberOfDigits = len(strNum)
    for i in range(numberOfDigits):
        rotatedNum = strNum[i:] + strNum[:i]
        rotations += [int(rotatedNum)]
    return rotations


MAX = 1000000

primes = [False] * MAX
for i in range(MAX):
    if i < 2:
        continue
    if is_prime(i):
        primes[i] = True


def allRotationsArePrime(n, primes):
    for rotation in allRotations(n):
        if not primes[rotation]:
            return False
    return True

allRotationsArePrimeCount = 0
for i in range(MAX):
    if allRotationsArePrime(i, primes):
        print(i)
        allRotationsArePrimeCount += 1

print(allRotationsArePrimeCount)

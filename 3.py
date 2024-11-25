import math


def isPrime(integer: int, primesList: list) -> object:
    if integer in primesList:
        return True
    for i in range(2, 1 + math.ceil(math.sqrt(integer))):
        if integer % i == 0:
            return False
    primesList += [integer]
    # print(primesList)
    return True


def findPrimeFactors(integer, primesList, factors):
    if isPrime(integer, primesList):
        factors += [integer]
        return factors
    for i in range(3, math.ceil(integer / 2), 2):
        if isPrime(i, primesList) and integer % i == 0:
            factors += [i]
            print("new: " + str(int(integer / i)))
            return findPrimeFactors(int(integer / i), primesList, factors)
    return factors

primesList = [2, 3, 5]

print(str(findPrimeFactors(600851475143, primesList, [])))
# print(str(primesList))
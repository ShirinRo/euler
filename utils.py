import math

def flatten_list(l):
    return [item for sublist in l for item in sublist]

def isPrime(integer: int, primesList: list) -> object:
    if integer in primesList:
        return True
    for i in range(2, 1 + math.ceil(math.sqrt(integer))):
        if integer % i == 0:
            return False
    primesList += [integer]
    return True

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def findPrimeFactors(integer, factors, isPrimeFunc = is_prime):
    if isPrimeFunc(integer):
        factors += [integer]
        return factors
    for i in range(2, 1 + math.ceil(integer / 2)):
        if isPrimeFunc(i) and integer % i == 0:
            factors += [i]
    return factors


# stolen from wikipedia "Proof of Euler's product formula"
def phi(n, isPrimeFunc = is_prime):
    if n == 0:
        return 0
    if isPrimeFunc(n):
        return n - 1
    factors = findPrimeFactors(n, [], isPrimeFunc)
    result = n
    for factor in set(factors):
        result *= (1 - 1/factor)
    return result



def divisors(n):
    return [i for i in range(1, math.ceil(n / 2)+1) if n % i == 0]


def is_pandigital(n, includeZero = False):
    strNum = str(n)
    numOfDigits = (9 + int(includeZero))
    if len(strNum) != numOfDigits:
        return False
    uniqueNums = set(list(strNum))
    if len(uniqueNums) != numOfDigits:
        return False
    if not includeZero:
        return '0' not in uniqueNums
    return True

def slimFindAllPermutations(maxDigit, includeZero = False):
    return findAllPermutations([], "", maxDigit, includeZero)


def findAllPermutations(nsToIgnore, stringSoFar, maxDigit, includeZero = False):
    if len(stringSoFar) == maxDigit + int(includeZero):
        return [stringSoFar]
    results = []
    for index in range(1 - int(includeZero), maxDigit + 1):
        if index not in nsToIgnore:
            mediumResult = stringSoFar + str(index)
            results += findAllPermutations(nsToIgnore + [index], mediumResult, maxDigit, includeZero)
    return results

def findPermutationsOfNumber(n):
    permutations = findPermutationsOfDigits(list(str(n)))
    return set(permutations)

def findPermutationsOfDigits(digitsToUse, stringSoFar = ""):
    if len(digitsToUse) == 0:
        return [stringSoFar]
    results = []
    for index, digit in enumerate(digitsToUse):
        if len(stringSoFar) == 0 and digit == "0":  # this is to avoid numbers starting with zero
            continue
        mediumResult = stringSoFar + str(digit)
        newDigitsToUse = digitsToUse[:index] + digitsToUse[index+1:]
        results += findPermutationsOfDigits(newDigitsToUse, mediumResult)
    return results

def isPalindromic(n):
    return n == int(str(n)[::-1])


def SieveOfEratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


def triplet(m, n):
    msq = m * m
    nsq = n * n
    return sorted([msq - nsq, 2 * m * n, msq + nsq])


def gcd(a, b):
    return math.gcd(a, b)


def primitive_pythagorean_triplets(max_value):
    triplets = []
    for m in range(1, max_value + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                triplets += [triplet(m, n)]
    return triplets



def non_primitve_pythagorean_triplets(max_value):
    """
    :param primitive_triplets: primitive pythagorean triplets, sorted from smallest to largest.
    :param max_value: i love shaul.
    :return: list of triplets with non-primitve multiplications of given triplets.
    """
    primitives = primitive_pythagorean_triplets(max_value)
    new_list = []
    for triplet in primitives:
        smallest = triplet[0]
        n = 1
        while smallest * n < max_value:
            new_list += [[x * n for x in triplet]]
            n += 1
    return new_list
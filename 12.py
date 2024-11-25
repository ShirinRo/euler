import math

def nth(n):
    return int((1 + n) * (n / 2))


def findPrimeFactors(integer, factors):
    for i in range(2, integer+1):
        if integer % i == 0:
            factors += [i]
            return findPrimeFactors(int(integer / i), factors)
    return factors


def countInList(list):
    retDict = dict()
    for i in list:
        if i in retDict.keys():
            retDict[i] = retDict[i] + 1
        else:
            retDict[i] = 1
    return retDict

num = 28
primes = findPrimeFactors(28, [])
print(str(countInList(primes)))

def smartNumDivisors(integer):
    primes = findPrimeFactors(integer, [])
    histOfPrimes = countInList(primes)
    numDivisors = 1
    for value in histOfPrimes.values():
        numDivisors *= (value + 1)
    return numDivisors


print(str(smartNumDivisors(21)))

def divisors(n):
    return [i for i in range(1, math.ceil(n / 2)+1) if n % i == 0] + [n]

def numDivisors(n):
    return len(divisors(n))

i = 1000
while True:
    s_nth = nth(i)
    div = smartNumDivisors(s_nth)
    if div > 500:
        print(i)
        print(nth(i))
        break
    i += 1
    if i % 100 == 0:
        print(i)


# print(smartNumDivisors(12375))
# print(nth(10000))
# print(nth(100000))
# print(nth(1000000))
# print(numDivisors(nth(2400)))

# currNumDivisors = 1
# i = 2000
# nnth = nth(2000)
# while currNumDivisors < 500:
#     currNumDivisors = numDivisors(nnth)
#     i += 1
#     nnth += i
#     if i % 5 == 0:
#         print(i)
#         print(currNumDivisors)

# currNumDivisors = 1
# currN = 100
# while currNumDivisors < 500:
#     currN *= 10
#     print(currNumDivisors)
#     currNumDivisors = numDivisors(nth(currN))
# print(currN)

# triangles = [int(nth(i)) for i in range(1, 7)]
# print(triangles)

# for i in range(100000, 1000000):
#     nnth = nth(i)
#     if nnth % 8817900 != 0:
#         continue
#     divs = divisors(nnth)
#     # if len(divs) > 500:
#     #     print("it's a bingo!: " + str(nnth))
#     print("nth: " + str(nnth) + " divisors: " + str(divs))
#     print("numDivisors: " + str(len(divs)))

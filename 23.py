from utils import *


def isAbundant(n):
    divs = divisors(n)
    sumdivs = sum(divs)
    return sumdivs > n


def canBeWrittenAsSumOfTwoAbundants(n, abundantNumbers, justAbs):
    for abNum in justAbs:
        if abNum > n:
            return False
        if abundantNumbers[n - abNum]:
            return True
    return False

maxNum = 28123
areAbundant = [False] * maxNum
justAbundant = []
for i in range(12, maxNum):
    # print(i)
    isAb = isAbundant(i)
    areAbundant[i] = isAb
    if isAb:
        justAbundant += [i]
    #     print(f"foundAb = {i}")

print("~~~~~~~~~~~~~~")

mysum = 0
for i in range(1, maxNum):
    if not canBeWrittenAsSumOfTwoAbundants(i, areAbundant, justAbundant):
        print(f"cantBeWritten: {i}")
        mysum += i

print(mysum)

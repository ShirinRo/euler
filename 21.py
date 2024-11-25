import math

def findDivisors(n):
    return [i for i in range(1, math.ceil(n / 2)+1) if n % i == 0]


foundVals = {}

def isAmicable(integer, foundVals: dict):
    divisors = findDivisors(integer)
    sumOfDivisors = sum(divisors)
    if sumOfDivisors in foundVals.keys():
        if foundVals[sumOfDivisors] == integer and sumOfDivisors != integer:
            return True
    return False



for i in range(10000):
    foundVals[i] = sum(findDivisors(i))

amicables = []
for i in range(10000):
    if isAmicable(i, foundVals):
        amicables += [i]

print(amicables)
print(sum(amicables))
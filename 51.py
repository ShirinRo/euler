import math
import itertools as it

maxNum = 1000000

def isPrime(integer: int) -> object:
    for i in range(2, 1 + math.ceil(math.sqrt(integer))):
        if integer % i == 0:
            return False
    return True


allPrimes = [False] * maxNum

for number in range(1, maxNum, 2):
    if (isPrime(number)):
        allPrimes[number] = True



def allOptionsForReplacing(number, minFamilySize):
    maxNumCharsToReplace = len(str(number)) - 1
    families = []
    for numChars in range(1, maxNumCharsToReplace + 1):
        combs = it.combinations(range(maxNumCharsToReplace), numChars)
        for combination in combs:
            family = []
            tempStrint = list(str(number))
            for digit in range(10):
                shouldAdd = True
                for index in combination:
                    if index == 0 and digit == 0:
                        shouldAdd = False
                        continue
                    if tempStrint[index] == str(digit):
                        shouldAdd = False
                        continue
                    tempStrint[index] = str(digit)
                replacement = int("".join(tempStrint))
                if shouldAdd and replacement != number and allPrimes[replacement]:
                    family += [replacement]
            if len(family) >= minFamilySize:
                # family.sort()
                # families += [family]
                print(family)
                return True
    return False

# print(allOptionsForReplacing(1039, 8))

# print(allOptionsForReplacing(23, 5))
# print(allOptionsForReplacing(23, 6))
# print(allOptionsForReplacing(23, 7))
# print(allOptionsForReplacing(56003, 6))
# print(allOptionsForReplacing(56003, 7))

for i in range(1, maxNum, 2):
    print(i)
    if not allPrimes[i]:
        continue
    if allOptionsForReplacing(i, 8):
        print(i)
        break

from utils import *

def is_drunkable(n, primebools):
    strNum = str(n)
    liststrnum = list(strNum)
    if 2 in liststrnum or 4 in liststrnum or 6 in liststrnum or 8 in liststrnum or 0 in liststrnum:
        return False
    if not is_prime(n):
        return False
    for i in range(1, len(strNum)):
        truncFromLeft = int(strNum[i:])
        if not is_prime(truncFromLeft):
            return False
        truncFromRight = int(strNum[:i])
        if not is_prime(truncFromRight):
            return False
    return True

# MAX = 400000
# primebools = [False] * MAX
# primes = []
# for i in range(2, MAX):
#     if isPrime(i, primes):
#         primebools[i] = True

print("foundPrimes!")
found = []
foundNum = 0
j = 11
while foundNum < 11:
    j += 1
    if is_drunkable(j, []):
        print(j)
        print(f"found {foundNum}")
        found += [j]
        foundNum += 1

print(found)
print(foundNum)
print(sum(found))
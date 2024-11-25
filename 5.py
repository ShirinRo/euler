import math

# largest = math.factorial(20)

firstTwenty = [i for i in range(20, 2, -1)]

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


primesOfTwenty = findPrimeFactors(20, [])
print(primesOfTwenty)
print(countInList(primesOfTwenty))

totHist = dict()
for i in range(2, 20):
    primeFactors = findPrimeFactors(i, [])
    hist = countInList(primeFactors)
    for key in hist.keys():
        if key not in totHist.keys() or totHist[key] < hist[key]:
            totHist[key] = hist[key]

print(totHist)
prod = 1
for key in totHist.keys():
    prod = math.pow(key, totHist[key]) * prod

print(str(prod))
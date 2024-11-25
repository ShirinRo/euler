from utils import *

def waysToGetValue(valueToGet, coins, waysSoFar, coinsUsed, matrix):
    if len(coins) == 0:
        return waysSoFar
    largestCoin = coins[-1] # 2
    if valueToGet > largestCoin:
        if len(coins) > 1:
            if (matrix[valueToGet][largestCoin] is not None):
                return matrix[valueToGet][largestCoin]
            coinsWithoutLargest = coins[:-1]
            waysWithLargest = waysToGetValue(valueToGet - largestCoin, coins, waysSoFar, coinsUsed + [largestCoin], matrix)
            waysWithoutLargest = waysToGetValue(valueToGet, coinsWithoutLargest, waysSoFar, coinsUsed, matrix)
            ways = waysWithLargest + waysWithoutLargest
            matrix[valueToGet][largestCoin] = ways
            return ways
        else:
            return waysToGetValue(valueToGet - largestCoin, coins, waysSoFar, coinsUsed + [largestCoin], matrix)
    if valueToGet < largestCoin:
        return waysToGetValue(valueToGet, coins[:-1], waysSoFar, coinsUsed, matrix)
    if valueToGet == largestCoin:
        if len(coins) > 1:
            return waysSoFar + waysToGetValue(valueToGet, coins[:-1], waysSoFar, coinsUsed, matrix) + 1
        else:
            return waysSoFar + 1





ways = 0
i = 10
MAX = 100

allPrimes = []
for i in range(MAX + 1):
    if is_prime(i):
        allPrimes += [i]

matrix = [[None for i in range(MAX+1)] for i in range(MAX+1)]
w = 0
i = 10
while w < 5000:
    w = waysToGetValue(i, allPrimes, 0, [], matrix)
    if w > 5000:
        print(i)
    else:
        i+= 1


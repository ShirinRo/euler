import math


def sol(n):
    matrix = [[0 for i in range(n+1)] for i in range(n+1)]
    for r in range(0, n + 1):
        for c in range(0, n + 1):
            if r == 0:
                matrix[r][c] = c
                continue
            if c == 0:
                matrix[r][c] = r
                continue
            if c == 1 or r == 1:
                matrix[r][c] = 1
                continue
            else:
                cur_coin = r
                if c - cur_coin < 1:
                    matrix[r][c] = matrix[r-1][c]
                elif c - cur_coin == r:
                    matrix[r][c] = matrix[r][c - r] + matrix[r-1][c]
                else:
                    matrix[r][c] = matrix[r][c - r] + matrix[r - 1][c]
                if c == r:
                    matrix[r][c] += 1
    return matrix[n][n] - 1


def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

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
        # print(coinsUsed + [largestCoin])
        if len(coins) > 1:
            return waysSoFar + waysToGetValue(valueToGet, coins[:-1], waysSoFar, coinsUsed, matrix) + 1
        else:
            return waysSoFar + 1


MAX = 100
matrix = [[None for i in range(MAX+1)] for i in range(MAX+1)]
w = waysToGetValue(MAX, list(range(1, MAX)), 0, [], matrix)
print(f"i: {100}. w = {w}")
print("~~~~~~")


print(sol(100))
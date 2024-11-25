coins = [1, 2, 5, 10, 20, 50, 100, 200]


def waysToGetValue(valueToGet, coins, waysSoFar, coinsUsed):
    if len(coins) == 0:
        return waysSoFar

    # valueToGet = 5
    largestCoin = coins[-1] # 2
    if valueToGet > largestCoin:
        if len(coins) > 1:
            coinsWithoutLargest = coins[:-1]
            waysWithLargest = waysToGetValue(valueToGet - largestCoin, coins, waysSoFar, coinsUsed + [largestCoin])
            waysWithoutLargest = waysToGetValue(valueToGet, coinsWithoutLargest, waysSoFar, coinsUsed)
            return waysWithLargest + waysWithoutLargest
        else:
            return waysToGetValue(valueToGet - largestCoin, coins, waysSoFar, coinsUsed + [largestCoin])
    if valueToGet < largestCoin:
        return waysToGetValue(valueToGet, coins[:-1], waysSoFar, coinsUsed)
    if valueToGet == largestCoin:
        print(coinsUsed + [largestCoin])
        if len(coins) > 1:
            return waysSoFar + waysToGetValue(valueToGet, coins[:-1], waysSoFar, coinsUsed) + 1
        else:
            return waysSoFar + 1



print(waysToGetValue(200, coins, 0, []))
# 5
# 2 2 1
# 2 1 1 1
# 1 1 1 1 1
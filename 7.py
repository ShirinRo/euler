import math


def isPrime(integer: int) -> bool:
    # if integer in primesList:
    #     return True
    for i in range(2, 2 + math.ceil(math.sqrt(integer))):
        if integer % i == 0:
            return False
    # primesList += [integer]
    # print(primesList)
    return True


count = 2
currNum = 3
wantedN = 10001
while count < wantedN:
    currNum += 2
    if isPrime(currNum):
        print(currNum)
        count += 1

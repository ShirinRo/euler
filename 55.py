from utils import *

def isLychrel(n):
    currNum = n
    for iteration in range(50):
        reversedNum = int(str(currNum)[::-1])
        currNum = currNum + reversedNum
        if isPalindromic(currNum):
            return False
    return True


numLychrel = 0
for i in range(10, 10000):
    # print(i)
    if isLychrel(i):
        print(f"is Lychrel: {i}")
        numLychrel += 1

print(numLychrel)
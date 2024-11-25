import utils as u

def is_pandigital(n):
    strNum = str(n)
    if len(strNum)!= 9:
        return False
    uniqueNums = set(list(strNum))
    return len(uniqueNums) == 9 and '0' not in uniqueNums


def findAllPermutations(nsToIgnore, stringSoFar, maxDigit):
    if len(stringSoFar) == maxDigit:
        return [stringSoFar]
    results = []
    for index in range(1, maxDigit + 1):
        if index not in nsToIgnore:
            mediumResult = stringSoFar + str(index)
            results += findAllPermutations(nsToIgnore + [index], mediumResult, maxDigit)
    return results


numbers = findAllPermutations([], "", 7)
currMax = 0
for number in numbers:
    if int(number) > currMax and u.is_prime(int(number)):
        currMax = int(number)


print(currMax)

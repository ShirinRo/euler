def findPrimeFactors(integer, factors):
    for i in range(2, integer+1):
        if integer % i == 0:
            factors += [i]
            return findPrimeFactors(int(integer / i), factors)
    return factors


def numPrimeFactors(n):
    return len(set(findPrimeFactors(n, [])))

count = 0
i = 10
N = 4
while count < N:
    if numPrimeFactors(i) == N:
        count += 1
    else:
        count = 0
    print(i)
    i += 1
print(i - N)
import math


def findPrimeFactors(integer, factors, dict):
    if integer in dict.keys():
        return dict[integer]
    for i in range(2, integer+1):
        if integer % i == 0:
            factors += [i]
            return findPrimeFactors(int(integer / i), factors, {})
    return factors


def isgcdone(n, d):
    factors = findPrimeFactors(d, [], {})
    for factor in factors:
        if n % factor == 0:
            return False
    return True

l = []
bef = 0.428569999899993
aft = 0.4285728571857156

dict = {}

for d in range(1, 1000000):
    for n in range(math.floor(bef * d), math.ceil(aft * d)):
        l += [[n, d, float(n/d)]]
    print(d)

s_l = sorted(l, key=lambda tup: tup[2])
for i in range(len(s_l)):
    if s_l[i][0] == 3 and s_l[i][1] == 7:
        j = i - 1
        while not isgcdone(s_l[j][0], s_l[j][1]):
            j -= 1
        print(s_l[j])
        break
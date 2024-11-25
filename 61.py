import math

def isTriangle(P):
    determinant = math.sqrt(1 + 8 * P)
    solution1 = (-1 + determinant) / 2
    return solution1 == int(solution1), solution1


def isSquare(P):
    return int(math.sqrt(P)) == math.sqrt(P), math.sqrt(P)


def isPentagonal(P):
    determinant = math.sqrt(1+24*P) / 6
    solution1 = 1/6 + determinant
    return solution1 == int(solution1), solution1


def isHexagonal(P):
    determinant = math.sqrt(1+8*P)
    solution1 = (1 + determinant) / 4
    return solution1 == int(solution1), solution1


def isHeptagonal(P):
    determinant = math.sqrt(9 + 40*P)
    solution1 = (3 + determinant) / 10
    return solution1 == int(solution1), solution1


def isOctagonal(P):
    determinant = math.sqrt(4 + 12*P)
    solution1 = (2 + determinant) / 6
    return solution1 == int(solution1), solution1


def octagonal(n):
    return (n ** 2) * 3 - 2 * n


def octagonals_under_10k():
    num = 0
    n = 10
    oct = []
    while num < 10000:
        num = octagonal(n)
        if num > 999 and num < 10000:
            oct += [num]
        n += 1
    return oct


def suffix(n):
    return str(n)[2:]

def prefix(n):
    return str(n)[:2]

def find_chain(cur_chain, types_found):
    last_suffix = suffix(cur_chain[-1][0])
    if int(last_suffix) < 10:
        return []
    if len(types_found) == 6:
        if last_suffix == prefix(cur_chain[0][0]):
            return cur_chain
        else:
            return []
    for i in range(1, 100):
        num = int(last_suffix) * 100 + i
        if 3 not in types_found and isTriangle(num)[0]:
            chainWithNum = find_chain(cur_chain + [(num, 3, isTriangle(num)[1])], types_found + [3])
            if len(chainWithNum):
                return chainWithNum
        if 4 not in types_found and isSquare(num)[0]:
            chainWithNum = find_chain(cur_chain + [(num, 4, isSquare(num)[1])], types_found + [4])
            if len(chainWithNum):
                return chainWithNum
        if 5 not in types_found and isPentagonal(num)[0]:
            chainWithNum = find_chain(cur_chain + [(num, 5, isPentagonal(num)[1])], types_found + [5])
            if len(chainWithNum):
                return chainWithNum
        if 6 not in types_found and isHexagonal(num)[0]:
            chainWithNum = find_chain(cur_chain + [(num, 6, isHexagonal(num)[1])], types_found + [6])
            if len(chainWithNum):
                return chainWithNum
        if 7 not in types_found and isHeptagonal(num)[0]:
            chainWithNum = find_chain(cur_chain + [(num, 7, isHeptagonal(num)[1])], types_found + [7])
            if len(chainWithNum):
                return chainWithNum
    return []

def matchesMoreThanOneType(n):
    return int(isTriangle(n)[0]) + int(isSquare(n)[0]) + int(isHexagonal(n)[0]) + int(isHeptagonal(n)[0]) + \
        int(isOctagonal(n)[0]) + int(isPentagonal(n)[0])

chainsFound = 0
octagonals = octagonals_under_10k()

for oct_num in octagonals:
    chain = find_chain([(oct_num, 8, isOctagonal(oct_num)[1])], [8])
    if len(chain):
        s = sum([x[0] for x in chain])
        chainsFound += 1
        print(chain)
        # for x in chain:
        #     if matchesMoreThanOneType(x[0]) > 1:
        #         print(f"in chain number {chainsFound}, n: {x[0]} matches: {matchesMoreThanOneType(x[0])}")
        print(f"chain: {chain}, sum: {s}")



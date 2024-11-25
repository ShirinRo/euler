import math

def pentagonal(n):
    return int(0.5 * n * (3 * n - 1))

def isPentagonal(P):
    determinant = math.sqrt(1+24*P) / 6
    solution1 = 1/6 + determinant
    return solution1 == int(solution1)


MAX = 10000
# pentagonals = [0]
# for n in range(1, MAX + 1):
#     pentagonals += [pentagonal(n)]

for i in range(1, MAX):
    for j in range(i+1, MAX):
        pi = pentagonal(i)
        pj = pentagonal(j)
        if isPentagonal(pi + pj):
            # print(f"i: {i}, j: {j}")
            if isPentagonal(pj - pi):
                print(pj - pi)
                break
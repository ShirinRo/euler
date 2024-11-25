import math

def triangle(n):
    return int((1 + n) * (n / 2))


def isPentagonal(P):
    determinant = math.sqrt(1+24*P) / 6
    solution1 = 1/6 + determinant
    return solution1 == int(solution1)


def isHexagonal(P):
    determinant = math.sqrt(1+24*P) / 6
    solution1 = 1/6 + determinant
    return solution1 == int(solution1)

n = 40755 # try 1, then set n as value of tri, and iterate
while True:
    n += 1
    tri = triangle(n)
    if isPentagonal(tri) and isHexagonal(tri):
        print(tri)
        break
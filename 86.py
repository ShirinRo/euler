import math
import numpy as np

def triplet(m, n):
    msq = m * m
    nsq = n * n
    return sorted([msq - nsq, 2 * m * n, msq + nsq])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def primitive_pythagorean_triplets(max_value):
    triplets = []
    for m in range(1, max_value + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                triplets += [triplet(m, n)]
    return triplets



def non_primitve_pythagorean_triplets(max_value):
    """
    :param primitive_triplets: primitive pythagorean triplets, sorted from smallest to largest.
    :param max_value: i love shaul.
    :return: list of triplets with non-primitve multiplications of given triplets.
    """
    primitives = primitive_pythagorean_triplets(max_value)
    new_list = []
    for triplet in primitives:
        smallest = triplet[0]
        n = 1
        while smallest * n < max_value:
            new_list += [[x * n for x in triplet]]
            n += 1
    return new_list

MAX_VALUE = 2000
newlist = non_primitve_pythagorean_triplets(MAX_VALUE)
print(newlist)


histogram = [0] * MAX_VALUE
for pythagoreanTriplet in newlist:
    first = pythagoreanTriplet[0]
    second = pythagoreanTriplet[1]
    if first < MAX_VALUE and 2 * first > second:
        histogram[first] += math.floor(second/2) - (second - first - 1)
    if second < MAX_VALUE:
        histogram[second] += math.floor(first / 2)

print(histogram)
print(sum(histogram))


cumsum = 0
index = 0
while cumsum < 1000000 and index < MAX_VALUE:
    cumsum += histogram[index]
    print(f"index: {index}, cumsum: {cumsum}")
    index += 1

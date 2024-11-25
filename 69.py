import math


def find_primes(n):
    arr = [i for i in range(n + 1)]
    for i in range(2, math.ceil(math.sqrt(n))):
        for k in range(2 * i, n + 1, i):
            arr[k] = 0
    return arr

n = 1000000
primes = find_primes(n)
arr = []
for i in range(n):
    arr += [1]
for i in range(2, n):
    print(i)
    if primes[i] == 0:
        continue
    arr[i] = i / (i - 1)
    for j in range(i + i, n, i):
        arr[j] /= (1 - (1 / i))


max_ratio = max(arr)
print(arr.index(max_ratio))
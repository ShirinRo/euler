import math

def find_primes(n):
    arr = [i for i in range(n + 1)]
    for i in range(2, math.ceil(math.sqrt(n))):
        for k in range(2 * i, n + 1, i):
            arr[k] = 0
    return arr

a = find_primes(200)
print(a)
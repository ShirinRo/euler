from utils import *

MAX = 100000
numbers = [False] * MAX
numbers[1] = True
primes = [2]

for i in range(3, MAX, 2):
    if is_prime(i):
        primes += [i]
        numbers[i] = True

print("created primes")

for k in range(MAX):
    if k % 2 == 0:
        numbers[k] = True
    for p in primes:
        n = p + 2 * (k ** 2)
        if n > MAX:
            break
        numbers[n] = True

print("good good")


for i, v in enumerate(numbers):
    if not v:
        print(i)
        break

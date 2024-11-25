import math

def isPrime(integer: int, primesList: list) -> object:
    if integer <= 1:
        return False
    if integer in primesList:
        return True
    for i in range(2, 1 + math.ceil(math.sqrt(integer))):
        if integer % i == 0:
            return False
    primesList += [integer]
    return True


primes = []
max_length = 0
prod = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        f = lambda x: x**2 + a*x + b
        i = 0
        length = 0
        while isPrime(f(i), primes):
            length += 1
            i += 1
        if length > max_length:
            max_length = length
            prod = a * b
    print(a)
print(prod)
print(max_length)


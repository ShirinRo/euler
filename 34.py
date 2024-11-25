import math as mt

def sumFactDigits(i):
    sum = 0
    for j in str(i):
        sum += mt.factorial(int(j))
    return sum

for i in range(1000000):
    if i == sumFactDigits(i):
        print(i)
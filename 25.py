import math

# phi = 0.5 * (1 + math.sqrt(5))
# psi = 0.5 * (1 - math.sqrt(5))
#
# def fib(n):
#     return int((pow(phi, n) - pow(psi, n)) / math.sqrt(5))

a = 1
b = 2
c = 3
i = 1
while len(str(a)) and len(str(b)) and len(str(c)) < 1000:
    i += 3
    a = b + c
    b = c + a
    c = a + b
    print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
    # if a % 2 == 0 and a < 4000000:
    #     sum += a
    # if b % 2 == 0 and b < 4000000:
    #     sum += b
    # if c % 2 == 0 and c < 4000000:
    #     sum += c


# i = 1
# while True:
#     strfib = str(fib(i))
#     print(i)
#     if len(strfib) >= 1000:
#         break
#     i += 1

print(i)
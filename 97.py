exponent = 7830457
seed = 28433
modulo = 10 ** 15

num = seed
for exp in range(exponent):
    num = (num << 1) % modulo
print(num + 1)
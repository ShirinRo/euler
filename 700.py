import math

# A = 1504170715041707
# B = 4503599627370517
A = 1512
B = 4575

def calc_num(n):
    return (A * n) % B

def calc_mod(b, n):
    return (A * n) % b


eulercoins = [calc_num(1)]
indices = [1]

cur = 1
while cur < 100000:
    n = calc_num(cur)
    if n < eulercoins[-1]:
        eulercoins += [n]
    cur += 1

print(eulercoins)
#
#
#
eulercoins = [calc_mod(B, 1)]
indices = [1]

while True:
    last_found_coin = eulercoins[-1]
    target = B - last_found_coin

    # n = math.floor(A / target) + 1
    i = 1
    while True:
        candidate = calc_mod(target, i)
        if candidate < last_found_coin:
            eulercoins += [candidate]
            break
        else:
            i+=1
        if candidate == 0:
            print(eulercoins)
            exit(1)

    # new_eulercoin = (n * A) % target
    if eulercoins[-1] == eulercoins[-2]:
        print(eulercoins)
        print(sum(eulercoins))
        exit(1)
    # eulercoins += [new_eulercoin]





import math
d = 1
i = 1
strnum = ""
prod = 1
while len(strnum) < 1000001:
    strnum += str(i)
    i += 1

for i in range(0, 7):
    prod *= int(strnum[10 ** i - 1])

print(prod)

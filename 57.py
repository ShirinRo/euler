numenator = 3
denomenator = 2

count = 0
for i in range(1000):
    print(f"{numenator} / {denomenator}")
    if len(list(str(numenator))) > len(list(str(denomenator))):
        count += 1
    new_numenator = numenator + 2 * denomenator
    denomenator = numenator + denomenator
    numenator = new_numenator

print(count)
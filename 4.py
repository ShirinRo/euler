top = 999
maxPal = 0
for i in range(100, top):
    for j in range(i, top):
        prod = str(i * j)
        # print(prod)
        # print(prod[::-1])
        if prod == prod[::-1] and int(prod) > maxPal:
            print(prod)
            maxPal = int(prod)
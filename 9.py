for a in range(3, 500):
    for b in range(a, 500):
        c = 1000 - a - b
        if (a**2 + b**2) == c**2:
            print(a * b * c)
            print("a:" + str(a) + " b:" + str(b) + " c:" + str(c))
            break

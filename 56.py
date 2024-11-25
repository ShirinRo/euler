def sumDigits(n):
    return sum([int(x) for x in list(str(n))])

MAX = 101
curr_max = 0
max_a = 0
max_b = 0
for a in range(1, 100):
    for b in range(1, 101):
        aPowB = a ** b
        sumDigs = sumDigits(aPowB)
        print(f"{a} ^ {b} = {aPowB} => {sumDigs}")
        if sumDigs > curr_max:
            curr_max = sumDigs
            max_a = a
            max_b = b

print("~~~~~~~~")
print(curr_max)
print(f"a: {max_a}, b: {max_b}")
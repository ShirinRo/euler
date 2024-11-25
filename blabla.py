a = 0
b = 1

while b < 10000:
    a += b
    print(f"{a}, {a / b}")
    b += a
    print(f"{b}, {b / a}")

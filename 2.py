
a = 1
b = 2
c = 3
sum = 2
while a < 4000000:
    a = b + c
    b = c + a
    c = a + b
    print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
    if a % 2 == 0 and a < 4000000:
        sum += a
    if b % 2 == 0 and b < 4000000:
        sum += b
    if c % 2 == 0 and c < 4000000:
        sum += c

print("sum = " + str(sum))
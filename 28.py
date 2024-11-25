N = 1001
s = 1
for i in range(3, N + 1, 2):
    for t in range(4):
        s += i ** 2 - t * (i -1)
print(s)
squares = [x ** 2 for x in range(10)]

def get_next(n):
    return sum([squares[int(x)] for x in str(n)])

c = 0
MAX = int(10 ** 7)
getTo1 = [False] * MAX
getTo89 = [False] * MAX
for i in range(1, MAX):
    print(c/MAX)
    if getTo1[i]:
        continue
    if getTo89[i]:
        c += 1
        continue
    n = i
    chain = [i]
    while n != 89 and n != 1:
        chain += [n]
        if getTo1[n]:
            n = 1
            break
        elif getTo89[n]:
            n = 89
            break
        n = get_next(n)
    for item in chain:
        if n == 1:
            getTo1[item] = True
        elif n == 89:
            getTo89[item] = True
            # print(i)

    c += int(n == 89)


print(c)
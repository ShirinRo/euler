dict = {}

def odd(n):
    return 3 * n + 1

def even(n):
    return n / 2

def chain(n):
    if n == 1:
        return 1
    if n in dict.keys():
        return dict[n]
    if n % 2 == 0:
        return chain(even(n)) + 1
    return chain(odd(n)) + 1


max_v = 0
max_i = 2

for i in range(2, 1000000):
    length = chain(i)
    if length > max_v:
        max_v = length
        max_i = i
    dict[i] = length

print(max_i)
print(max_v)


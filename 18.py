# day5Input = open('eu18input', 'r')
day5Input = open('p067_triangle.txt', 'r')
lines = day5Input.readlines()
numbers = []
for line in lines:
    numbers += [[int(i) for i in line.split()]]

print(numbers)


row = 0
col = 0
mytuples = []


for i in range(len(numbers)):
    if i == 0:
        n = numbers[0][0]
        numbers[0][0] = [n, n]
        continue

    for j in range(len(numbers[i])):
        if j == 0:
            n = numbers[i][j]
            max_p = numbers[i - 1][j][1]
            my_p = max_p + n
            numbers[i][j] = [n, my_p]
            continue
        if j == len(numbers[i]) - 1:
            n = numbers[i][j]
            max_p = numbers[i - 1][j - 1][1]
            my_p = max_p + n
            numbers[i][j] = [n, my_p]
            continue
        n = numbers[i][j]
        max_p = max(numbers[i-1][j-1][1], numbers[i-1][j][1])
        my_p = max_p + n
        numbers[i][j] = [n, my_p]

print(max([i[1] for i in numbers[-1]]))
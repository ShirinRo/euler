import numpy as np
day5Input = open('p81_matrix.txt', 'r')
lines = day5Input.readlines()
numbers = []
for line in lines:
    numbers += [[int(i) for i in line.split(',')]]
matrix = np.array(numbers)
trans = np.transpose(matrix)
for row in range(80):
    for col in range(80):
        prev_options = []
        if row > 0:
            prev_options += [trans[row - 1][col]]
        if col > 0:
            prev_options += [trans[row][col - 1]]
        if len(prev_options) == 0:
            continue
        trans[row][col] += min(prev_options)
print(trans[79][79])
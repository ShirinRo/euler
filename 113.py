import numpy as np
from math import comb

def get_num_inc_mat(k):
    mat = np.zeros((k, 9))
    for row in range(k):
        for digit in range(8, -1, -1):
            if row == 0 or digit == 8:
                mat[row][digit] = 1
            else:
                mat[row][digit] = mat[row - 1][digit] + mat[row][digit + 1]
    return mat

def get_num_dec_mat(k):
    mat = np.zeros((k, 9))
    for row in range(k):
        for digit in range(9):
            if row == 0:
                mat[row][digit] = 1
            elif digit == 0:
                mat[row][digit] = row + 1
            else:
                mat[row][digit] = mat[row - 1][digit] + mat[row][digit - 1]
    return mat

def get_num_inc(k):
    mat = get_num_inc_mat(k)

my_mat = get_num_inc_mat(4)
print(my_mat)

def dogs(i, j):
    return comb(i+j, i)

for i in range(1, 7):
    print(dogs(8, i))

MAXIMUM = 6
sum_increasing = 0
sum_decreasing = 0



for num_digits in range(MAXIMUM + 1):
    sum_increasing += dogs(8, num_digits)
    sum_decreasing += dogs(9, num_digits)

print(f"increasing: {sum_increasing}")
print(f"decreasing: {sum_decreasing}")
num_both = 9 * MAXIMUM
print(f"both: {num_both}")

#### WHY (- MAXIMUM - 2)??? there is not enough room here in order to explain.
print(f"total: {sum_increasing +sum_decreasing - num_both - MAXIMUM - 2 }")

### also, without the for loop:
print(f'increasing? {dogs(9, MAXIMUM)}')
print(f'decreasing? {dogs(10, MAXIMUM)}')

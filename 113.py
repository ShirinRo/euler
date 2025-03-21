import numpy as np

def get_num_inc(k):
  mat = np.zeros((k, 9))
  for i in range(k):
    for j in range(9):
      if i == 0:
        mat[i][j] = 9 - j
      else:
        for l in range(j, 9):
          mat[i][j] += mat[i-1][l]
  return mat


my_mat = get_num_inc(6)
sum = my_mat[5].sum()
print(sum)

def get_num_dec(k):
  mat = np.zeros((k, 9))
  for i in range(k):
    for j in range(9):
      if i == 0:
        mat[i][j] = 10 - j
      else:
        for l in range(j, 9):
          mat[i][j] += mat[i-1][l]
  return mat

my_mat = get_num_dec(3)
print(my_mat)
# sum = sum + my_mat[5].sum()
# print(sum)

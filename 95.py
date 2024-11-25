import math
import numpy as np


def sum_of_shaul_da_king(n):
    arr = np.zeros(n + 1, dtype=int)
    arr[1] = 1
    for i in range(1, n + 1):
        k = 2 * i
        while k <= n:
            arr[k] += i
            k += i
    return arr

MAX = 1000000
should_skip = np.zeros(MAX + 1, dtype=bool)
good_mat = sum_of_shaul_da_king(MAX)
max_chain_length = 0
min_num_in_max_chain = math.inf
for num in range(2, MAX):
    if should_skip[num]:
        continue
    print(num)
    cur_chain = [num]
    next_num = good_mat[num]
    while next_num < MAX and not should_skip[next_num] and next_num not in cur_chain:
        cur_chain += [next_num]
        next_num = good_mat[next_num]
    if num == next_num:
        if len(cur_chain) > max_chain_length:
            max_chain_length = len(cur_chain)
            min_num_in_max_chain = min(cur_chain)
        elif len(cur_chain) == max_chain_length:
            min_num_in_max_chain = min(min(cur_chain), min_num_in_max_chain)
    for chain_member in cur_chain:
        if chain_member <= num:
            should_skip[chain_member] = True


print(max_chain_length)
print(min_num_in_max_chain)
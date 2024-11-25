# import math
# import time
# import numpy as np
# import itertools
#
#
# def getSlice(n, s, e, length):
#     return (n // (10 ** (length - e))) % (10 ** (e - s))
#
#
# def dogs(n: int, l: list):
#     if sum(l) == n:
#         return True
#     for index in range(1, len(l)+1):
#         prefix_nums = [str(x) for x in l[:index]]
#         prefix = int("".join(prefix_nums))
#         if prefix > n:
#             continue
#         if dogs(n - prefix, l[index:]):
#             return True
#     return False
#
#
# def dogsHelper(sqrt_n: int, n: int, l: list, merge_size: int, n_length: int):
#     if sum(l) == sqrt_n:
#         return True
#     for index in range(0, n_length - merge_size):
#         merged = getSlice(n, index, index + merge_size, n_length)
#         new_l = l[:index] + [merged] + l[index + merge_size:]
#         if sum(new_l) > sqrt_n:
#             continue
#         if dogs(sqrt_n, new_l):
#             return True
#     return False
#
#
# def isNumberS(n, sqrt_of_n):
#     numbers = [int(x) for x in list(str(n))]
#     return dogsHelper(sqrt_of_n, n, numbers, max(len(str(sqrt_of_n))-1, 1), len(numbers))
#
#
# def hopefully_fast_is_number_s(n, sqrt_n, all_matrics):
#     numbers = [int(x) for x in list(str(n))]
#     vecs = all_matrics[len(numbers) - 1]
#     return sqrt_n in np.array(numbers) * vecs
#
#
# def generate_vectors(n_length) -> np.ndarray:
#     lst = list(map(list, itertools.product([0, 1], repeat=n_length - 1)))
#     binary_lists = [l + [1] for l in lst]
#     for bin_list in binary_lists:
#         for i in range(n_length - 1, -1, -1):
#             if bool(bin_list[i]):
#                 continue
#             bin_list[i] = bin_list[i + 1] * 10
#     return np.asmatrix(binary_lists).transpose()
#
#
#
#
# MAX = 10**12
# sqrtmax = round(math.sqrt(MAX))
# sumofSs2 = 0
#
# all_matrices = []
# for i in range(1, 14):
#     all_matrices += [generate_vectors(i)]
#
# for i in range(2, sqrtmax + 1):
#     if i % 10000 == 0:
#         print(i/sqrtmax)
#     if hopefully_fast_is_number_s(i * i, i, all_matrices):
#         sumofSs2 += i ** 2
#
# print(sumofSs2)
#
#
# ------------------------------
#



import math
import numpy as np
import itertools
import time


def generate_vectors(n_length) -> np.ndarray:
    binary_lists = list(map(lambda x: list(x) + [1], itertools.product([0, 1], repeat=n_length - 1)))
    for bin_list in binary_lists:
        for i in range(n_length - 1, -1, -1):
            if bool(bin_list[i]):
                continue
            bin_list[i] = bin_list[i + 1] * 10
    return np.asmatrix(binary_lists).transpose()

timebef = time.perf_counter()
all_matrices = []
for i in range(1, 13):
    all_matrices += [generate_vectors(i)]
print(f"time for creating matrices: {time.perf_counter() - timebef}")


def is_s(n, sqrt_n, all_matrics):
    numbers = [int(x) for x in list(str(n))]
    vecs = all_matrics[len(numbers) - 1]
    return sqrt_n in np.array(numbers) * vecs


MAX = 10**12
sqrtmax = math.sqrt(MAX)
sum_of_s = int(sqrtmax)

timebef = time.perf_counter()
for i in range(9, int(sqrtmax), 9):
    # if i % 10000 == 0:
    #     print(i/sqrtmax)
    if is_s(i * i, i, all_matrices):
        # print(i)
        sum_of_s += i ** 2

for i in range(10, int(sqrtmax), 9):
    # if i % 10000 == 0:
    #     print(i/sqrtmax)
    if is_s(i * i, i, all_matrices):
        # print(i)
        sum_of_s += i ** 2

print(sum_of_s)
print(f"time it took: {time.perf_counter() - timebef} seconds")
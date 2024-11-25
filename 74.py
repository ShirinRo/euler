import math
from utils import *
import itertools as it
import time

def get_fac_sum(n):
    return sum([math.factorial(int(x)) for x in list(str(n))])


def get_chain(n):
    l = []
    while n not in l:
        l += [n]
        n = get_fac_sum(n)
    return l

def get_chain_smart(n, arr):
    l = []
    while n not in l:
        key = list(str(n))
        key.sort()
        key = int("".join(key))
        if arr[key] != 0:
            return arr[n] + len(l)
        l += [n]
        n = get_fac_sum(n)
    return len(l)

def slow_solution(n):
    MAX = n
    c = 0
    for i in range(1, MAX + 1):
        chain = get_chain(i)
        if len(chain) == 60:
            c += 1
    return c


def fast_sol(n):
    arr = [0] * (3 * 10 ** 6)
    for i in range(1, n + 1):
        if arr[i] != 0:
            continue
        chain_len = get_chain_smart(i, arr)
        arr[i] = chain_len
        ### this solution was before Jonathan suggested I just sort the number to find the key (i.e. 5043 -> 0345 -> 345)
        # perms = it.permutations(list(str(i)))
        # for perm in perms:
        #     if perm[0] == "0":
        #         continue
        #     arr[int("".join(perm))] = chain_len

    c = 0
    for i in range(1, n + 1):
        if arr[i] == 60:
            c += 1
    return c

start_time = time.perf_counter()
# print(slow_solution(10 ** 6))
mid_time = time.perf_counter()
print(f"count: {fast_sol(10 ** 6)}")
end_time = time.perf_counter()

print(f"slow took: {mid_time - start_time}, fast took: {end_time - mid_time}")
from utils import *


def calc_factors_of(n):
    return calc_factors_helper(n, is_initial=True)


# returns all the possible combinations of divisors whose products are n,
# e,g for n = 12 it will return [[2, 2, 3], [2, 2, 3], [3, 4], [2, 6]]
# notice it's not unique
def calc_factors_helper(n, is_initial=False):
    if n == 1:
        return [[]]
    if is_prime(n):
        return [[n]]
    lists_to_return = []
    target = math.floor(n / 2) + 1 if is_initial else n + 1
    for i in range(2, target):
        if n % i == 0:
            factors_lists_with_i = calc_factors_helper(n // i)
            for factors_list in factors_lists_with_i:
                lists_to_return += [[i] + factors_list]
    return lists_to_return


print(calc_factors_of(16))

MAX = 12000
ks = [0] * (MAX + 1)
for n in range(1, 2 * MAX + 1):
    print(n)
    if is_prime(n):
        continue
    factors_lists = calc_factors_helper(n, True)
    for factors_list in factors_lists:
        factors_sum = sum(factors_list)
        factors_product = n
        if factors_sum > factors_product:
            print(f"aha: {n}")
        diff = factors_product - factors_sum
        k = len(factors_list) + diff
        if k <= MAX and (n < ks[k] or ks[k] == 0):
            ks[k] = n

print(set(ks))
print(sum(set(ks)))


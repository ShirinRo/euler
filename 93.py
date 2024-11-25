import itertools


def permutations_of_digits(digits_list) -> [int]:
    return [list(x) for x in list(itertools.permutations(digits_list))]


def find_max_n(list_of_sorted_ints):
    counter = 1
    for integer in list_of_sorted_ints:
        if integer == counter:
            counter += 1
            continue
        else:
            return counter - 1


digit_sets = list(itertools.combinations(range(1, 10), 4))

mul_func = lambda x, y: x * y
div_func = lambda x, y: x / y
plus_func = lambda x, y: x + y
minus_func = lambda x, y: x - y
operations = [mul_func, div_func, plus_func, minus_func]

# digit_sets = [[1, 2, 3, 4]]
max_max_n = 1
max_digit_set = []
for digit_set in digit_sets:
    nums_created_by_set = []
    permutations_of_set = permutations_of_digits(digit_set)
    for permutation in permutations_of_set:
        a, b, c, d = permutation
        for operation1 in operations:
            ab = operation1(a, b)
            for operation2 in operations:
                abc = operation2(ab, c)
                for operation3 in operations:
                    abcd = operation3(abc, d)
                    if abcd >= 1 and abcd % 1 == 0:
                        nums_created_by_set += [int(abcd)]
                for operation4 in operations:
                    cd = operation4(c, d)
                    for operation5 in operations:
                        abcd = operation5(ab, cd)
                        if abcd >= 1 and abcd % 1 == 0:
                            nums_created_by_set += [int(abcd)]
    sorted_unique = sorted(list(set(nums_created_by_set)))
    max_n = find_max_n(sorted_unique)
    if max_n > max_max_n:
        max_max_n = max_n
        max_digit_set = digit_set
print(f"digits: {max_digit_set}, max n: {max_max_n}")


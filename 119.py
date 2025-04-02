def sum_of_digits(num: int):
    num_as_str = str(num)
    return sum([int(x) for x in num_as_str])

# print(sum_of_digits(512))

good_nums = []
for n in range(2, 100):
    print(f'#### {n} / 100')
    for p in range (2, 10):
        num = n ** p
        if sum_of_digits(num) == n:
            good_nums += [num]

print(sorted(good_nums)[29])

#


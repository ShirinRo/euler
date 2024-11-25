import itertools

def contain_all_squares(group_a: list, group_b: list):
    return groups_contain_num(group_a, group_b, 0, 1) and groups_contain_num(group_a, group_b, 0, 4) and \
        groups_contain_num(group_a, group_b, 0, 9) and groups_contain_num(group_a, group_b, 1, 6) and \
        groups_contain_num(group_a, group_b, 2, 5) and groups_contain_num(group_a, group_b, 3, 6) and \
        groups_contain_num(group_a, group_b, 4, 9) and groups_contain_num(group_a, group_b, 6, 4) and \
        groups_contain_num(group_a, group_b, 8, 1)


def groups_contain_num(group_a, group_b, number1, number2):
    return (number1 in group_a and number2 in group_b) or (number1 in group_b and number2 in group_a)

def extend_group_if_needed(group):
    if 6 in group and 9 not in group:
        return group + [9]
    elif 9 in group and 6 not in group:
        return group + [6]
    else:
        return group

combinations = list(itertools.combinations(range(10), 6))
combs_as_lists = []
for combination in combinations:
    combs_as_lists += [[int(x) for x in list(combination)]]

count = 0
for comb_a in combs_as_lists:
    for comb_b in combs_as_lists:
        if comb_b == comb_a:
            continue
        if contain_all_squares(extend_group_if_needed(comb_a), extend_group_if_needed(comb_b)):
            count += 1


print(count)
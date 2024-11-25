def is_pandigital(multiplicand, multiplier, product):
    char_multiplicand = [x for x in str(multiplicand)]
    char_multiplier = [x for x in str(multiplier)]
    char_product = [x for x in str(product)]
    all_digits = char_multiplicand + char_multiplier + char_product
    if len(all_digits) != 9:
        return False
    return set(all_digits) == {"1", "2", "3", "4", "5", "6", "7", "8", "9"}


cool_prods = []
for multiplicand in range(1, 9999):
    print(multiplicand)
    for multiplier in range(1,9999):
        prod = multiplier * multiplicand
        if (len(str(prod)) + len(str(multiplicand)) + len(str(multiplier))) > 9:
            break
        if is_pandigital(multiplicand, multiplier, prod):
            cool_prods += [prod]
            # print(f"{multiplicand} * {multiplier} = {prod}")


print(set(cool_prods))
mysum = sum(set(cool_prods))
print(mysum)
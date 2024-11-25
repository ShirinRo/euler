# hassam elion is 1,000,000 since 7 * 9^5 < 1,000,000

def is_equal_to_fifth_power_of_digits(n):
    sum_digits = sum([int(x) ** 5 for x in str(n)])
    if sum_digits == n:
        print(i)
        return n
    else:
        return 0

mysum = 0
for i in range(2, 1000000):
    mysum += is_equal_to_fifth_power_of_digits(i)



print(mysum)
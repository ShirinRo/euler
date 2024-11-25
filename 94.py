import math
import utils

def area_of_equilateral(a, b):
    return b * math.sqrt(a * a - b * b / 4) / 2

# perimeter = 0
# a = 1
# max_perimeter = 1000000000
# sum_perims = 0
# last_area = 0
# last_perim = 0
# last_a = 0
# last_last_a = 0
# while a < max_perimeter / 3 + 1:
#     a += 1
#     b1 = a + 1
#     b2 = a - 1
#
#     area_ab = area_of_equilateral(a, b1)
#     if area_ab % 1 == 0 and a + a + b1 <= max_perimeter:
#         print(f"{a}, {a}, b1: {b1} -> {area_ab}")
#         sum_perims += a + a + b1
#         last_last_a = last_a
#         last_a = a
#         print(f"formula: {last_a * 4 - last_last_a}")
#     area_ba = area_of_equilateral(a, b2)
#     if area_ba % 1 == 0 and a + a + b2 <= max_perimeter:
#         print(f"{a}, {a}, b2: {b2} -> {area_ba}")
#         sum_perims += a + a + b2
#         last_last_a = last_a
#         last_a = a
#         last_last_a = last_a
#         last_a = a
#         print(f"formula: {last_a * 4 - last_last_a}")
#     # print(f"done: {100 * a / (max_perimeter / 3 + 1)}%")
#
# print(sum_perims)


prev_a = 5
a = 17
multiplier = 1
perimeter_sum = 2 * 5 + 6 + 2 * 17 + 16
while a < 1000000000 // 3 + 1:
    new_a = a * 4 - prev_a + 2 * multiplier
    multiplier *= -1
    new_perimeter = 3 * new_a - multiplier
    if new_perimeter > 1000000000:
        break
    print(f"{new_a},{new_a}, {new_a - multiplier}")
    prev_a = a
    a = new_a
    perimeter_sum += new_perimeter

print(f"sum = {perimeter_sum}")
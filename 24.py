import numpy as np


def blabla(nsToIgnore, string, maxN):
    results = []
    for index in range(maxN):
        if index not in nsToIgnore:
            results += [string + str(index)]
    return results


def addMissingNumbers(nsToIgnore, stringSoFar, maxDigit):
    if len(stringSoFar) == maxDigit + 1:
        return [stringSoFar]
    results = []
    for index in range(maxDigit + 1):
        if index not in nsToIgnore:
            mediumResult = stringSoFar + str(index)
            results += addMissingNumbers(nsToIgnore + [index], mediumResult, maxDigit)
    return results


numbers = addMissingNumbers([], "", 9)
print(numbers[999999])
# perms = []
# for i in range(4):
#     mystr = str(i)
#     perms += blabla(i, mystr, 4)

mystr = ""

# print(perms)
#
# def perms(n):
#     strs = []
#     arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     ptr = n - 1
#     counter = 0
#     flag = True
#     while flag:
#         my_strrr = ''.join(map(str, arr))
#         a = [c for c in my_strrr]
#         if len(set(a)) == len(a):
#             counter += 1
#             if counter == 1000000:
#                 print(my_strrr)
#                 break
#         arr[ptr] += 1
#         if arr[ptr] > 9:
#             while arr[ptr] > 9:
#                 for i in range(ptr, n):
#                     arr[i] = 0
#                 ptr = ptr - 1
#                 if ptr < 0:
#                     flag = False
#                     break
#                 arr[ptr] += 1
#             ptr = n - 1
#     permutations = []
#     return permutations



# def is_unique(n):
#     chars = [c for c in str(n)]
#     return len(set(chars)) == len(chars)
#
#
# target = 274240
# counter = 0
# print(is_unique(123))
# for i in range(2000000000, 3000000000):
#     if is_unique(i):
#         print(counter)
#         counter += 1
#         if counter == target:
#             print(i)

import itertools

def listOfIntsToInt(l):
    return int("".join([str(x) for x in l]))


ints = []
permutations = list(itertools.permutations(range(1, 11)))
for permutation in permutations:
    asList = [int(x) for x in list(permutation)]
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = asList
    outer = [x1, x9, x4, x10, x7]
    line1 = [x1, x2, x3]
    line2 = [x9, x3, x5]
    line3 = [x4, x5, x6]
    line4 = [x10, x6, x8]
    line5 = [x7, x8, x2]
    if sum(line1) == sum(line2) == sum(line3) == sum(line4) == sum(line5):
        minXinOuter = min(outer)
        if minXinOuter in line1:
            ints += [listOfIntsToInt(line1 + line2 + line3 + line4 + line5)]
        if minXinOuter in line2:
            ints += [listOfIntsToInt(line2 + line3 + line4 + line5 + line1)]
        if minXinOuter in line3:
            ints += [listOfIntsToInt(line3 + line4 + line5 + line1 + line2)]
        if minXinOuter in line4:
            ints += [listOfIntsToInt(line4 + line5 + line1 + line2 + line3)]
        if minXinOuter in line5:
            ints += [listOfIntsToInt(line5 + line1 + line2 + line3 + line5)]

ints.sort()
only_16_d = [x for x in ints if len(str(x)) == 16]
print(only_16_d[-1])

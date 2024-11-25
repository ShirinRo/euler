inputfile = open("p079_keylog.txt", "r")
loginattempts = inputfile.readlines()
loginattempts = set([x.rstrip('\n') for x in loginattempts])

allDigits = set([item for sublist in loginattempts for item in sublist])
print(allDigits)


def goodSort(setOfDigits):
    if len(setOfDigits) == 0:
        return []
    digit = setOfDigits.pop()
    left = []
    right = []
    for attempt in loginattempts:
        ind = attempt.find(digit)
        if ind != -1:
            left += attempt[:ind]
            right += attempt[ind + 1:]
    left = set(left).intersection(setOfDigits)
    right = set(right).intersection(setOfDigits)
    return goodSort(list(left)) + [digit] + goodSort(list(right))

print("".join(goodSort(allDigits)))
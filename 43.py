from utils import *


permutations = slimFindAllPermutations(9, True)
s = 0
if "1406357289" in permutations:
    print("good")
for permutation in permutations:
    print(permutation)
    if permutation[0] == "0":
        continue
    num = int(permutation)
    if int(permutation[1:4]) % 2 == 0 and \
        int(permutation[2:5]) % 3 == 0 and \
        int(permutation[3:6]) % 5 == 0 and \
        int(permutation[4:7]) % 7 == 0 and \
        int(permutation[5:8]) % 11 == 0 and \
        int(permutation[6:9]) % 13 == 0 and \
        int(permutation[7:10]) % 17 == 0:
        s += num

print(s)
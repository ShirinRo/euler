import re

letters = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

s = 0

def str_2_digit(i):
    if len(str(i)) > 2:
        print("asdasdasd")
        return
    stringnum = str(i)
    if i in letters.keys():
        return len(letters[i])
    if len(stringnum) == 2:
        ones = i % 10
        tens = i - ones
        return len(letters[ones]) + len(letters[tens])

s = 0
for i in range(1, 1000):
    if i < 100:
        s += str_2_digit(i)
    else:
        if i % 100 != 0:
            s += 3 + str_2_digit(i % 100)
        s += len("hundred") + str_2_digit(int(i/100))

    # if len(stringnum) == 3:
    #     ones = i % 10
    #     tens = ((i - ones) / 10) % 10
    #     hundreds = (i - ones - (tens * 10)) / 100
    #     s += len(letters[hundreds])
    #     s += len("hundred")
    #     thestring += letters[hundreds]
    #     thestring += "hundred"
    #     if tens != 0 or ones != 0:
    #         s += len("and")
    #         thestring += "and"
    #     real_tens = tens * 10 + ones
    #     if real_tens < 21:
    #         s += len(letters[real_tens])
    #         thestring += letters[real_tens]
    #     elif real_tens in letters.keys():
    #         s += len()
    #     else:
    #         if tens != 0:
    #             s += len(letters[tens])
    #             thestring += letters[tens]
    #         if ones != 0:
    #             s += len(letters[ones])
    #             thestring += letters[ones]
    # print(f"{thestring} - {i}")

s += len("onethousand")



print(s)
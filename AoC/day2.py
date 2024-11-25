import re

input = open('2input', 'r')
passwords = input.readlines()

countValid = 0
minimum = 0
maximum = 100
line: str
for line in passwords:
    match = re.match(r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)", line)
    # print("\n~~~~~~\n")
    # print("line = " + line)
    # print("min = " + match.group(1))
    # print("max = " + match.group(2))
    # print("letter = " + match.group(3))
    # print("password = " + match.group(4))
    min = int(match.group(1))
    max = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    # countOfLetter = password.count(letter)
    # if countOfLetter >= min and countOfLetter <= max:
    if max > len(password):
        print("password: ", + password, ", max: " + max)
        continue
    first = password[min-1]
    second = password[max-1]
    if (first == letter) ^ (second == letter):
        countValid += 1
        print("first: " + first + " , second: " + second)
        print("V " + line)
    else:
        print("X" + line)
print(countValid)

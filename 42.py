import math as m

wordsfile = open('p042_words.txt', 'r')
words = wordsfile.readlines()[0].split(",")


def calcWordValue(word):
    sum = 0
    for letter in list(word):
        if letter == '"':
            continue
        sum += ord(letter) - 64
    return sum


def isIntRoot(t):
    determinant = m.sqrt(1+8*t) / 2
    solution1 = - 0.5 + determinant
    return solution1 == int(solution1)

count = 0

for word in words:
    value = calcWordValue(word.upper())
    if isIntRoot(value):
        count += 1

print(count)

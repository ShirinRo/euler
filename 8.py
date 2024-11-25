longNum = open('eu8input', 'r')
lines = longNum.readlines()

neighbors = 13
largestProduct = 1
# for lineNum, line in enumerate(lines):
#     for i in range(len(line) - 1):
#         if i + neighbors < len(line) - 1:
#             hslice = line[i:i+neighbors]
#             prod = 1
#             for j in hslice:
#                 prod *= int(j)
#             if prod > largestProduct:
#                 largestProduct = prod
        # if lineNum + neighbors < len(lines):
        #     vprod = 1
        #     for row in range(lineNum, lineNum + neighbors + 1):
        #         print(":: " + lines[row][i])
        #         vprod *= int(lines[row][i])
        #     if vprod > largestProduct:
        #         largestProduct = vprod

longLine = ""
for line in lines:
    longLine += line[:len(line)-1]
for i in range(len(longLine)):
    if i + neighbors < len(longLine):
        hslice = longLine[i:i+neighbors]
        prod = 1
        for j in hslice:
            prod *= int(j)
        if prod > largestProduct:
            largestProduct = prod

print(largestProduct)


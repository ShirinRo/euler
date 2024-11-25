day5Input = open('5input', 'r')
passes = day5Input.readlines()

maxID = 0
ids = []
for boardingPass in passes:
    row = 0
    for i in range(7):
        if boardingPass[i] == "B":
            row += 2 ** (6 - i)
    col = 0
    for j in range(7, 10):
        if boardingPass[j] == "R":
            col += 2 ** (9 - j)
    id = 8 * row + col
    ids += [id]
    maxID = max(id, maxID)
    # print("row: " + str(row) + ", col: " + str(col) + ", id: " + str(id))

print(maxID)
ids.sort()

print(str(ids[1:-1]))
for id in ids[1:-1]:
    if id + 1 not in ids and id + 2 in ids:
        print(id+1)



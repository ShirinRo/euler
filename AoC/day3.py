mapinput = open('3input', 'r')
tobmap = mapinput.readlines()

countTrees = 0
line: str
locx = 0
locy = 1
print(tobmap[0])

for line in tobmap[1:]:
    locy += 1
    if locy % 2 == 0:
        print(line)
        continue
    locx += 1
    locx = locx % 31
    editedLine = line
    if line[locx] == "#":
        countTrees += 1
        editedLine = line[:locx] + "X" + line[locx+1:]
    else:
        editedLine = line[:locx] + "O" + line[locx+1:]
    print(editedLine)

print(countTrees)

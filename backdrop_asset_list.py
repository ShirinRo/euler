myinput = open('model.txt', 'r')
lines = myinput.readlines()

# for line in lines:
#     if "assetName" in line:
#         print(line.split()[1])

for line in lines:
    if "value" in line:
        if line.split()[1] != "{":
            print(line.split()[1])

for line in lines:
    if "thumbnailURL" in line:
        print(line.split()[1])

for line in lines:
    if "name" in line:
        print(line.split()[1])

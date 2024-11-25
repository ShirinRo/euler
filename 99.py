import math

inputfile = open("p099_base_exp.txt", "r")
base_exp = inputfile.readlines()
base_exp = [x.rstrip('\n') for x in base_exp]

max_line = 0
max_value = 0

for line_num, value in enumerate(base_exp):
    x, y = [int(x) for x in value.split(",")]
    if math.log2(x) * y > max_value:
        max_line = line_num
        max_value = math.log2(x) * y

print(max_line)

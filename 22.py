lower_l = [x.lower() for x in l]
lower_l.sort()
i = 0
s = 0
while i < len(lower_l):
    name = list(lower_l[i])
    values = [ord(x) - 96 for x in name]
    s += sum(values) * (i + 1)
    i += 1
print(s)
# (a + b + c + d)^2 = a^2 + b^2 + c^2 + d^2 + 2ab + 2ac + 2ad + 2bc + 2bd + 2cd, based on this we only need the 2s

top = 100
sum = 0
for i in range(1, top + 1):
    for j in range(i+1, top + 1):
       sum += 2 * i * j


print(str(sum))
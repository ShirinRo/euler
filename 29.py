max = 101
terms = []
for a in range(2, max):
    for b in range(2, max):
        terms += [a ** b]

terms.sort()

print(terms)
print(len(set(terms)))
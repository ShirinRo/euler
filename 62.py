
perm_to_count = {}
perm_to_min = {}

didFind = False
i = 1
while not didFind:
    print(i)
    cubed = i ** 3
    sorted_cubed = list(str(cubed))
    sorted_cubed.sort()
    sorted_cubed = "".join(sorted_cubed)
    if sorted_cubed in perm_to_count.keys():
        perm_to_count[sorted_cubed] += 1
        if perm_to_count[sorted_cubed] == 5:
            print(perm_to_min[sorted_cubed])
            didFind = True
    else:
        perm_to_count[sorted_cubed] = 1
        perm_to_min[sorted_cubed] = cubed
    i += 1

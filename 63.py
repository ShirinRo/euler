count = 0
for p in range(1, 50):
    for d in range(1, 10):
        if len(str(d ** p)) == p:
            count += 1
            print(f"found with p = {p}")

print(count)
closest = (0, 0)
closest_val = 0
C = 8 * 10 ** 6

for w in range(1, 100):
    for h in range(w, 100):
        val = w * (w + 1) * h * (h + 1)
        if abs(C - val) < abs(C - closest_val):
            closest = (w, h)
            closest_val = val

print(f"w: {closest[0]} h: {closest[1]} area: {closest[0] * closest[1]}")
print(closest_val)
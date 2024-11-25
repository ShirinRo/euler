for a in range(11, 100):
    for b in range(a+1, 100):
        frac = a/b
        digits_a = list(str(a))
        digits_b = list(str(b))
        if digits_a[1] == "0" and digits_b[1] == "0":
            continue
        intersection = set(digits_a).intersection(set(digits_b))
        if len(intersection) == 0:
            continue
        intersection = intersection.pop()
        digits_a.remove(intersection)
        digits_b.remove(intersection)
        if digits_b[0] == "0":
            continue
        if int(digits_a[0]) / int(digits_b[0]) == frac:
            print(a, b)
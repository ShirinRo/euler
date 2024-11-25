def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def is_right_triangle(p1, p2, p3):
    d12 = dist(p1, p2)
    d13 = dist(p1, p3)
    d23 = dist(p3, p2)
    if d12 == max(d12, d13, d23):
        return d12 == d13 + d23
    elif d13 == max(d12, d13, d23):
        return d13 == d12 + d23
    else:
        return d23 == d12 + d13


def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0


def generate_all_points(n):
    l = []
    for x in range(n + 1):
        for y in range(n + 1):
            l += [(x, y)]
    return l


p1 = (0, 0)
MAX = 50
c = 0
points = generate_all_points(MAX)
for i in range(len(points)):
    for j in range(i, len(points)):
        p2 = points[i]
        p3 = points[j]
        if is_collinear(p1, p2, p3):
            continue
        if is_right_triangle(p1, p2, p3):
            c += 1
            print(f"{p2}, {p3}")
print(c)
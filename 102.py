

def is_origin_in_vectors(source, p1, p2):
    v1 = [p1[0] - source[0], p1[1] - source[1]]
    v2 = [p2[0] - source[0], p2[1] - source[1]]
    determinant = v1[0]*v2[1] - v1[1]*v2[0]
    if determinant == 0:
        return False
    determinant = 1 / determinant
    inverse_v1 = [determinant * v2[1], determinant * -1 * v2[0]]
    inverse_v2 = [determinant * -1 * v1[1], determinant * v1[0]]
    a = source[0] * inverse_v1[0] + source[1] * inverse_v1[1]
    b = source[0] * inverse_v2[0] + source[1] * inverse_v2[1]
    print('a',a)
    print('b',b)
    return a < 0 and b < 0 and a >= -1 and b >= -1

# is_origin_in_vectors([-1, -5], [3, 3], [-3, 2])
inputfile = open("0102_triangles.txt", "r")
lines = inputfile.readlines()

triangles = [line.strip().split(',') for line in lines]
# triangle1 = ['-1', '1', '4', '1', '-1', '-3']
# triangles = [triangle1]
good_triangles = 0
for triangle in triangles:
    p1 = [int(coordinate) for coordinate in triangle[:2]]
    p2 = [int(coordinate) for coordinate in triangle[2:4]]
    p3 = [int(coordinate) for coordinate in triangle[4:]]

    if is_origin_in_vectors(p1, p2, p3): # and is_origin_in_vectors(p2, p3, p1) and is_origin_in_vectors(p3, p1, p2):
        good_triangles += 1

print(good_triangles)
import numpy as np
myinput = open('p82_matrix.txt', 'r')
lines = myinput.readlines()
numbers = []
for line in lines:
    numbers += [[int(i) for i in line.split(',')]]
# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]
matrix = numbers

class Node:
    def __init__(self, value):
        self.value = value
        self.distance = np.infty
        self.prev = None
        self.neighbors = []
    def __repr__(self):
        return str(self.distance)

visited = []
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        value = matrix[row][col]
        matrix[row][col] = Node(value)
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        currNode: Node = matrix[row][col]
        if col < len(matrix[0]) - 1:
            currNode.neighbors += [matrix[row][col + 1]]
        if row > 0:
            currNode.neighbors += [matrix[row - 1][col]]
        if row < len(matrix) - 1:
            currNode.neighbors += [matrix[row + 1][col]]
shortestPath = np.infty
startNode = Node(0)
endNode = Node(0)

for row in range(len(matrix)):
    startNode.neighbors += [matrix[row][0]]
    matrix[row][len(matrix) - 1].neighbors += [endNode]
startNode.distance = 0
queue = [startNode]

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        queue.append(matrix[c][r])
queue.append(endNode)

while len(queue) > 0:
    queue.sort(key=lambda x: x.distance)
    currNode = queue[0]
    neighbors = currNode.neighbors
    for neighbor in neighbors:
        newDist = currNode.distance + neighbor.value
        if newDist < neighbor.distance:
            neighbor.distance = newDist
            neighbor.prev = currNode
    queue.remove(currNode)
# # for v in queue:
# #     for neighbor in v.neighbors:
# #         v.distance = min(v.distance, v.value + neighbor.distance)
#
print(endNode.distance)
# print(matrix)
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __eq__(self, other):
        return self.value == other.value

class CircleJerk:
    def __init__(self, input, max):
        nodes = [Node(value=x) for x in input]
        for i in range(len(input)):
            next_index = (i + 1) % len(input)
            nodes[i].next = nodes[next_index]
        nodes.sort(key=self.val)
        self._cups = nodes
        self.max = max

    def val(self, node):
        return node.value

    def inOrder(self) -> str:
        cup = self._cups[0]
        s = str(cup.value)
        for _ in range(len(self._cups) - 1):
            cup = cup.next
            s += ", " + str(cup.value)
        return s

    def __repr__(self):
        cup = self._cups[0]
        s = f"{cup.next.value} * {cup.next.next.value} = {int(cup.next.value) * int(cup.next.next.value)}"
        return s


    def move(self, current):
        a = current.next
        b = a.next
        c = b.next
        value_to_ret = c.next
        removed_values = [x.value for x in [a, b, c]]

        current.next = c.next
        value_to_search = current.value - 1
        destination = None
        while destination is None:
            if value_to_search in removed_values:
                value_to_search -= 1
                continue
            if value_to_search == 0:
                value_to_search = self.max
                continue
            destination = self._cups[value_to_search - 1]

        after_dest = destination.next
        destination.next = a
        c.next = after_dest
        return value_to_ret


prod = [9, 4, 2, 3, 8, 7, 6, 1, 5]
test = [3, 8, 9, 1, 2, 5, 4, 6, 7]

input = prod
start = 8
max = 1000000
steps = max * 10

for i in range(10, max + 1):
    input += [i]

example = CircleJerk(input, max)
print(example.inOrder())
a = example._cups[start]
for i in range(steps):
    print(steps - i)
    a = example.move(a)
    # print("next current: " + str(a.value))
    # print(example.inOrder())
    # print(example)
print(example)

day5Input = open('eu13input', 'r')
numbers = day5Input.readlines()
print(numbers)
nums = []
for i in numbers:
    nums += [int(i[:-35])]
print(nums)

s = 0
for k in nums:
    s += k
print(s)
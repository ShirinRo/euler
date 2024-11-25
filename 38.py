def is_pandigital(n):
    strNum = str(n)
    if len(strNum)!= 9:
        return False
    uniqueNums = set(list(strNum))
    return len(uniqueNums) == 9 and '0' not in uniqueNums


max = 918273645
for i in range(9123, 9877):
    n = int(str(i) + str(i * 2))
    if is_pandigital(n) and n > max:
        max = n

print(max)
input = open("p059_cipher.txt", "r")
nums = input.read()

numbers = nums.split(",")
print(numbers)

print(ord('a')) # 97
print(len(numbers))


def containsAllCommons(string: str):
    common = ["of ", "the "]
    for word in common:
        if string.find(word) == -1:
            return False
    return True

for a in range(97, 97+26):
    for b in range(97, 97+26):
        for c in range(97, 97+26):
            key = [a, b, c]
            xord = []
            for index, number in enumerate(numbers):
                xord += [chr(int(number) ^ key[index % 3])]
            strxord = "".join(xord)
            if containsAllCommons(strxord):
                asciisum = sum([ord(x) for x in xord])
                print(f"sum = {asciisum}")
                print(key)
                print(strxord)


def isPalindromic(n):
    return n == int(str(n)[::-1])


MAX = 1000000
s = 0
for i in range(MAX):
    if not isPalindromic(i):
        continue
    bin_i = bin(i)[2:]
    if not isPalindromic(int(bin_i)):
        continue
    s += i

print(s)
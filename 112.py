def is_increasing(num_as_str):
    prev_letter = None
    for letter in num_as_str:
        if prev_letter is None:
            prev_letter = letter
            continue
        if int(letter) < int(prev_letter):
            return False
        else:
            prev_letter = letter
    return True

def is_decreasing(num_as_as_str):
    num_as_as_str = reversed(num_as_as_str)
    return is_increasing(num_as_as_str)

def is_bouncy(num):
    num_as_str = str(num)
    is_this_increasing = is_increasing(num_as_str)
    is_this_decreasing = is_decreasing(num_as_str)
    return not is_this_decreasing and not is_this_increasing


percent = 0
num_bouncy = 0
i = 1
while i < 1000000:
    if is_bouncy(i):
        num_bouncy += 1

    percent = num_bouncy / i
    i += 1
    print(i)

print(num_bouncy)


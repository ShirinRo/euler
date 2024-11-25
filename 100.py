import math

MAX = 10e12
blue = 1
prev_good_blue = 1
guess_red = 1
ratio = 0.4
guess_blue = 1
last_diff = 0
while blue < MAX:
    blue += 1
    if blue % 1000 == 0:
        print(blue)
    for red in range(guess_red, math.ceil(blue * 0.42) + 1):  # 0.42 is the upper bound to the red/blue ratio
        probability = blue * (blue - 1) / ((red + blue) * (red + blue - 1))
        if probability == 0.5:
            print(f"~~~~~~~~~~")
            print(f"blue: {blue}, red: {red}")
            good_blue = blue
            ratio = good_blue / prev_good_blue
            print(f"ratio between this blue and previous blue: {ratio}")
            red_to_blue = red / good_blue
            print(f"red to blue ratio: {red_to_blue}")

            last_diff = good_blue - guess_blue
            print(f"diff = {last_diff}")

            prev_good_blue = good_blue
            blue = round(prev_good_blue * ratio)
            guess_red = round(red * ratio)
            guess_blue = blue
            blue += last_diff - 1  # minus 1 because we're doing blue += 1 after this (beginning of loop)
            print(f"new guess: blue: {blue}, red: {guess_red}")
            print(f"~~~~~~~~~~")
            break






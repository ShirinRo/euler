x = 0
m = 7
frog_location = 4
shot_location = 0

guess_n = 0
guess_m = 1
k = 0

for i in range(0, 50):
    shot_location = guess_n + i * guess_m
    if shot_location == frog_location:
        print(f"win! {frog_location}")
        break
    else:
        print(f"miss!")

    k += 1
    frog_location += m
    shot_location += guess_m
    print(f"frog: {frog_location}, shot: {shot_location}")

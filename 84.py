import random

CCpile = ["GO", "G2J", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

CHpile = ["GO", "G2J", "C1", "E3", "H2", "R1", "nextR", "nextR", "nextU", "goback3", 9, 10, 11, 12, 13, 14]

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
         "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP",
         "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J",
         "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

count = [0] * 40

CCpiles = ["CC1", "CC2", "CC3"]
CHpiles = ["CH1", "CH2", "CH3"]

random.shuffle(CCpile)
random.shuffle(CHpile)
print(CCpile)
print(CHpile)
curr_position = 0
doubles_count = 0

rounds = 500000

for i in range(rounds):
    dice1 = random.randint(1, 4)
    dice2 = random.randint(1, 4)
    if dice1 == dice2:
        doubles_count += 1
    else:
        doubles_count = 0

    if doubles_count == 3:
        doubles_count = 0
        curr_position = 10
        count[curr_position] += 1
        continue

    curr_position = (curr_position + dice1 + dice2) % len(board)
    board_position = board[curr_position]

    if board_position == "G2J":
        curr_position = 10
        count[curr_position] += 1
        continue

    if board_position in CHpiles:
        CHcard = CHpile[0]
        CHpile = CHpile[1:] + [CHcard]
        if CHcard == "GO":
            curr_position = 0
        elif CHcard == "G2J":
            curr_position = 10
        elif CHcard == "C1":
            curr_position = 11
        elif CHcard == "E3":
            curr_position = 24
        elif CHcard == "H2":
            curr_position = 39
        elif CHcard == "R1":
            curr_position = 5
        elif CHcard == "nextR":
            if 5 <= curr_position < 15:
                curr_position = 15
            elif 15 <= curr_position < 25:
                curr_position = 25
            elif 25 <= curr_position < 35:
                curr_position = 35
            else:
                curr_position = 5
        elif CHcard == "nextU":
            if 12 <= curr_position < 28:
                curr_position = 28
            else:
                curr_position = 12
        elif CHcard == "goback3":
            curr_position -= 3
            board_position = board[curr_position]


    if board_position in CCpiles:
        CCcard = CCpile[0]
        CCpile = CCpile[1:] + [CCcard]
        if CCcard == "GO":
            curr_position = 0
        elif CCcard == "G2J":
            curr_position = 10
    count[curr_position] += 1

count = [(c / rounds) * 100 for c in count]
joined = [(board[i], count[i]) for i in range(40)]
joined.sort(key=lambda x: x[1], reverse=True)
print(joined)
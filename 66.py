import math
from fractions import Fraction


def calc_next_term(original_n, nominator, denominator):
    new_denominator = original_n - denominator ** 2
    f = Fraction(nominator, new_denominator)
    nominator = f.numerator
    new_denominator = f.denominator
    addition = math.floor((nominator * (math.sqrt(original_n) + denominator)) / new_denominator)
    new_nominator = abs(nominator * denominator - addition * new_denominator)
    return addition, new_nominator, new_denominator


def get_period(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return []
    numerator = 1
    denumnator = int(math.sqrt(n))
    period = []
    values = []
    while True:
        addition, denumnator, numerator = calc_next_term(n, numerator, denumnator)
        if (addition, numerator, denumnator) in values:
            return period
        period += [addition]
        values += [(addition, numerator, denumnator)]



def expand(first_n, seq):
    seq.reverse()
    cur_den = Fraction(1, seq[0])
    seq = seq[1:]
    for i in seq:
        cur_den = Fraction(1, (i + cur_den))
    return Fraction(first_n, 1) + cur_den

max_x = 0
good_d = 0
for D in range(3, 1000):
    if math.sqrt(D) == int(math.sqrt(D)):
        continue
    period = get_period(D)
    if len(period) % 2 == 1:
        period = period + period
    period = period[:-1]
    frac: Fraction = expand(int(math.sqrt(D)), period)
    x = frac.numerator
    y = frac.denominator
    print(f"{x}^2 - {D} * {y} ^ 2 = 1")
    print("-----")
    if x > max_x:
        max_x = x
        good_d = D

print(f"max d: {good_d}")

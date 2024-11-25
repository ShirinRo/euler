from math import floor
import math
from fractions import Fraction

def seq(n):
    first_term = floor(sqrt(n))

    return 1

def calc_next_term(original_n, nominator, denominator):
    new_denominator = original_n - denominator ** 2
    f = Fraction(nominator, new_denominator)
    nominator = f.numerator
    new_denominator = f.denominator
    addition = floor((nominator * (math.sqrt(original_n) + denominator)) / new_denominator)
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


c = 0
for i in range(1, 10001):
    if len(get_period(i)) % 2 == 1:
        c += 1

print(c)
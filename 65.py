from fractions import Fraction


def next(first_n, seq):
    seq.reverse()
    cur_den = Fraction(1, seq[0])
    seq = seq[1:]
    for i in seq:
        cur_den = Fraction(1, (i + cur_den))
    return Fraction(first_n, 1) + cur_den


def sum_of(n):
    seq = [1, 2] + [item for sublist in [[1, 1, x] for x in range(4, 100, 2)] for item in sublist]
    seq = seq[:n-1]
    f = next(2, seq)
    return sum([int(x) for x in str(f.numerator)])


print(sum_of(100))
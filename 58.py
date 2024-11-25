from utils import *

number_on_diagonal = 1
number_of_primes = 0
ratio = 0.5
side_length = 1
while ratio > 0.1:
    side_length += 2
    x = side_length - 1
    top_left = x ** 2 + 1
    bottom_right = (x + 1) ** 2
    top_right = top_left - x
    bottom_left = bottom_right - x
    number_of_primes += int(is_prime(top_left))
    number_of_primes += int(is_prime(top_right))
    number_of_primes += int(is_prime(bottom_left))
    number_on_diagonal += 4
    ratio = number_of_primes / number_on_diagonal
print(side_length)


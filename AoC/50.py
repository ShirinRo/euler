from utils import *

MAX = 1000000

primes = [2]
for i in range(3, 10000, 2):
    if is_prime(i):
        primes += [i]

max_length = 0
seq = []
for seq_length in range(2, len(primes)):
    for index in range(0, len(primes) - seq_length):
        sub_seq = primes[index: index + seq_length]
        seq_sum = sum(sub_seq)
        if max_length < len(sub_seq) and seq_sum < MAX and is_prime(seq_sum):
            max_length = len(sub_seq)
            seq = sub_seq
print(max_length)
print(seq)
print(sum(seq))
from lib.more_itertools import count_items
from lib.sequences import collatz_sequence

result = 0
max_length = 0

for seed in range(1, 1_000_000):
    length = count_items(collatz_sequence(seed))

    if length > max_length:
        result = seed
        max_length = length

print(result)

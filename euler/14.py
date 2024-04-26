from lib import collatz_sequence

result = 0
max_length = 0

for seed in range(1, 1_000_000):
    length = sum(1 for _ in collatz_sequence(seed))

    if length > max_length:
        result = seed
        max_length = length

print(result)

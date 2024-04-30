from operator import itemgetter

from lib.more_itertools import count_items
from lib.sequences import collatz_sequence

sequences = ((seed, count_items(collatz_sequence(seed))) for seed in range(1, 1_000_000))
result = max(sequences, key=itemgetter(1))
print(result[0])

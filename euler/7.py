from lib.more_itertools import drop
from lib.sequences import primes

print(next(drop(primes(), 10000)))

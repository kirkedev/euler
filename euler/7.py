from lib.more_itertools import drop
from lib.sequences import primes

print(next(drop(10000, primes())))

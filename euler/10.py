from itertools import takewhile

from lib.sequences import primes

print(sum(takewhile(lambda prime: prime < 2_000_000, primes())))

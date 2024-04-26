from itertools import takewhile

from lib import primes

print(sum(takewhile(lambda prime: prime < 2_000_000, primes())))

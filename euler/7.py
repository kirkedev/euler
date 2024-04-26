from itertools import islice

from lib import primes

print(next(islice(primes(), 10000, 10001)))

from itertools import takewhile

from lib.factors import is_divisible_by
from lib.sequences import fibonacci

fibs = takewhile(lambda n: n < 4_000_000, fibonacci())
print(sum(filter(is_divisible_by(2), fibs)))

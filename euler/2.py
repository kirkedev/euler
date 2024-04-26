from itertools import takewhile

from lib import fibonacci, is_divisible_by

fibs = takewhile(lambda n: n < 4_000_000, fibonacci())
print(sum(filter(is_divisible_by(2), fibs)))

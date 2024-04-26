from itertools import count

from lib import is_divisible

print(next(number for number in count(1) if all(is_divisible(number, factor) for factor in range(20, 1, -1))))

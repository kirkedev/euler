from lib.factors import factors
from lib.more_itertools import count_items
from lib.sequences import triangular_numbers

print(next(number for number in triangular_numbers() if count_items(factors(number)) >= 500))

from itertools import starmap
from operator import add

from lib.sequences import amicable_pairs

print(sum(starmap(add, amicable_pairs(10000))))

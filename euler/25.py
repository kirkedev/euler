from itertools import count

from lib.sequences import fibonacci

print(next(index for (index, number) in zip(count(1), fibonacci()) if len(str(number)) == 1000))

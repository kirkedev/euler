from itertools import takewhile

from lib.more_itertools import count_if
from lib.sequences import dates

date_range = takewhile(lambda date: date.year < 2001, dates(1901))
print(count_if(lambda date: date.day == 1 and date.weekday() == 6, date_range))

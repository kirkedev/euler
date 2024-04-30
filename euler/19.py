from lib.more_itertools import count_if, flatten
from lib.sequences import dates

date_range = flatten(dates(year) for year in range(1900, 2001))
print(count_if(lambda date: date.day == 1 and date.weekday() == 6, date_range))

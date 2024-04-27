from lib.more_itertools import count_letters
from lib.spell_number import spell_number

print(sum(count_letters(spell_number(number)) for number in range(1, 1001)))

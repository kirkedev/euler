from itertools import count

from lib.text import alphabetic_positions

names = [name[1:-1] for name in open("res/0022_names.txt").read().split(",")]

print(sum(row * sum(alphabetic_positions(name)) for (row, name) in zip(count(1), sorted(names))))

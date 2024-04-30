from lib.sequences import fibonacci

print(next(index + 1 for (index, number) in enumerate(fibonacci()) if len(str(number)) == 1000))

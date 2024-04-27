from lib import squares

numbers = range(1, 101)
print(sum(numbers) ** 2 - sum(squares(numbers)))

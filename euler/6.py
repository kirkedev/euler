from lib import squared

numbers = range(1, 101)
print(sum(numbers) ** 2 - sum(squared(numbers)))

from lib import squares

numbers = range(1, 101)
square_of_sums = sum(numbers) ** 2
sum_of_squares = sum(squares(numbers))

print(square_of_sums - sum_of_squares)

from lib import factors, triangular_numbers

print(next(number for number in triangular_numbers() if sum(1 for _ in factors(number)) >= 500))

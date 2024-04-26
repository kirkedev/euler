from lib import is_divisible_by

is_multiple_of_three = is_divisible_by(3)
is_multiple_of_five = is_divisible_by(5)

print(sum(number for number in range(1, 1000) if is_multiple_of_three(number) or is_multiple_of_five(number)))

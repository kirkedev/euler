from lib.numeric import is_palindromic_number, products

print(max(filter(is_palindromic_number, products(range(1, 1000)))))

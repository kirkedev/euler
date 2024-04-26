from lib import triplets

print(next(a * b * c for a, b, c in triplets(1000) if a + b + c == 1000))

from itertools import permutations

digits = sorted(permutations(range(0, 10)))[999_999]
print("".join(map(str, digits)))

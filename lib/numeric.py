from itertools import combinations
from math import prod
from typing import Iterable

from lib.text import is_palindrome


def is_palindromic_number(number: int) -> bool:
    return is_palindrome(str(number))


def squared(numbers: Iterable[int]) -> Iterable[int]:
    return (number ** 2 for number in numbers)


def products(numbers: Iterable[int]) -> Iterable[int]:
    return map(prod, combinations(numbers, 2))

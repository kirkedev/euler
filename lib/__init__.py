import re
from functools import lru_cache
from itertools import combinations
from math import prod
from typing import Callable, Iterable, TypeVar, Tuple

from lib.factors import is_divisible

T = TypeVar("T")
Coordinates = Direction = Dimensions = Tuple[int, int]
Predicate = Callable[[T], bool]


def is_palindrome(string: str) -> bool:
    stripped = re.sub(r"[\W\s]", "", string.lower())
    return stripped == stripped[::-1]


def is_palindromic_number(number: int) -> bool:
    return is_palindrome(str(number))


def squares(numbers: Iterable[int]) -> Iterable[int]:
    return (number ** 2 for number in numbers)


@lru_cache
def count_edges(row: int, column: int) -> int:
    return 1 if row == 0 or column == 0 else count_edges(row - 1, column) + count_edges(row, column - 1)


def products(numbers: Iterable[int]) -> Iterable[int]:
    return map(prod, combinations(numbers, 2))

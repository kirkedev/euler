from collections import defaultdict
from itertools import count, combinations
from typing import Iterable

from lib import is_divisible


def fibonacci() -> Iterable[int]:
    last = 0
    result = 1

    while True:
        last, result = result, last + result
        yield result


def primes():
    marked = defaultdict(list)

    for number in count(2):
        if number in marked:
            for multiple in marked.pop(number):
                marked[number + multiple].append(multiple)
        else:
            yield number
            marked[number * number].append(number)


def triplets(stop: int):
    return ((a, b, c) for a, b, c in combinations(range(1, stop), 3) if a < b < c and a ** 2 + b ** 2 == c ** 2)


def triangular_numbers() -> Iterable[int]:
    for i in count(2):
        yield sum(range(i))


def collatz_sequence(number: int) -> Iterable[int]:
    yield number

    while number > 1:
        number = number // 2 if is_divisible(number, 2) else 3 * number + 1
        yield number

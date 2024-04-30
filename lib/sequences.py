from _operator import add
from collections import defaultdict
from datetime import date
from itertools import count, combinations, starmap, product, tee, chain
from typing import Iterable, Tuple

from lib.factors import is_divisible, proper_divisors
from lib.more_itertools import window


def fibonacci() -> Iterable[int]:
    last = 0
    result = 1

    yield 1

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


def dates(year: int) -> Iterable[date]:
    for year in count(year):
        for month in range(1, 13):
            end = 1

            if month in (4, 6, 9, 11):
                end += 30
            elif month == 2:
                end += 29 if is_divisible(year, 4) and not is_divisible(year, 100) else 28
            else:
                end += 31

            for day in range(1, end):
                yield date(year, month, day)


def amicable_pairs(stop: int) -> Iterable[Tuple[int, int]]:
    paired = []

    for number in range(1, stop):
        if number in paired:
            continue

        other = sum(proper_divisors(number))

        if number != other and sum(proper_divisors(other)) == number:
            paired.append(other)
            yield number, other


def non_abundant_sums() -> Iterable[int]:
    abundant_numbers = (number for number in range(1, 28124) if sum(proper_divisors(number)) > number)
    numbers = sorted(set(number for number in starmap(add, product(*tee(abundant_numbers))) if number < 28124))

    for first, last in window(chain([0], numbers, [28124]), 2):
        yield from range(first + 1, last)

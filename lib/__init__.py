import re
from collections import defaultdict, deque
from functools import partial, lru_cache
from itertools import combinations, islice, count, chain
from math import sqrt, ceil, isqrt, prod
from typing import Callable, Iterable, TypeVar, Tuple

T = TypeVar("T")
Coordinates = Direction = Dimensions = Tuple[int, int]


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def is_divisible_by(divisor: int) -> Callable[[int], bool]:
    return partial(is_divisible, divisor=divisor)


def fibonacci() -> Iterable[int]:
    last = 0
    result = 1

    while True:
        last, result = result, last + result
        yield result


def is_prime(number: int) -> bool:
    return False if number == 1 else not any(is_divisible(number, divisor) for divisor in range(2, number))


def factors(number: int) -> Iterable[int]:
    numbers = []

    for factor in range(1, ceil(sqrt(number))):
        if is_divisible(number, factor):
            yield factor
            numbers.append(number // factor)

    square = isqrt(number)

    if square ** 2 == number:
        yield square

    yield from reversed(numbers)


def prime_factors(number: int) -> Iterable[int]:
    return filter(is_prime, factors(number))


def is_palindrome(string: str) -> bool:
    stripped = re.sub(r"[\W\s]", "", string.lower())
    return stripped == stripped[::-1]


def products(numbers: Iterable[int]) -> Iterable[int]:
    return map(prod, combinations(numbers, 2))


def is_palindromic_number(number: int) -> bool:
    return is_palindrome(str(number))


def squares(numbers: Iterable[int]) -> Iterable[int]:
    return (number ** 2 for number in numbers)


def window(iterable: Iterable[T], size: int) -> Iterable[Iterable[T]]:
    iterator = iter(iterable)
    result = deque(islice(iterator, size - 1), maxlen=size)

    for item in iterator:
        result.append(item)
        yield tuple(result)


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
        number = number / 2 if is_divisible(number, 2) else 3 * number + 1
        yield number


def flatten(iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    return chain(*iterable)


@lru_cache
def count_edges(row: int, column: int) -> int:
    return 1 if row == 0 or column == 0 else count_edges(row - 1, column) + count_edges(row, column - 1)

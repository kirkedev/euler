from functools import partial
from itertools import takewhile
from math import ceil, sqrt
from typing import Callable, Iterable


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def is_divisible_by(divisor: int) -> Callable[[int], bool]:
    return partial(is_divisible, divisor=divisor)


def factors(number: int) -> Iterable[int]:
    numbers = []
    root = ceil(sqrt(number))

    for factor in range(1, root):
        if is_divisible(number, factor):
            yield factor
            numbers.append(number // factor)

    if root ** 2 == number:
        yield root

    yield from reversed(numbers)


def is_prime(number: int) -> bool:
    return False if number == 1 else not any(is_divisible(number, divisor) for divisor in range(2, number))


def prime_factors(number: int) -> Iterable[int]:
    return filter(is_prime, factors(number))


def proper_divisors(number: int) -> Iterable[int]:
    return takewhile(lambda n: n < number, factors(number))

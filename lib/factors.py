from functools import partial
from math import ceil, sqrt, isqrt
from typing import Callable, Iterable


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def is_divisible_by(divisor: int) -> Callable[[int], bool]:
    return partial(is_divisible, divisor=divisor)


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


def is_prime(number: int) -> bool:
    return False if number == 1 else not any(is_divisible(number, divisor) for divisor in range(2, number))


def prime_factors(number: int) -> Iterable[int]:
    return filter(is_prime, factors(number))

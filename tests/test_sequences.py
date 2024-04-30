from itertools import takewhile

from lib.factors import is_prime, factors
from lib.more_itertools import take, count_items
from lib.sequences import primes, triangular_numbers, collatz_sequence, fibonacci, dates, amicable_pairs


def test_primes():
    assert list(take(10, primes())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert all(is_prime(number) for number in take(100, primes()))


def test_triangular_numbers():
    assert list(take(10, triangular_numbers())) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert next(number for number in triangular_numbers() if count_items(factors(number)) >= 5) == 28


def test_collatz_sequence():
    assert list(collatz_sequence(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_fibonacci():
    assert list(take(5, fibonacci())) == [1, 1, 2, 3, 5]


def test_dates():
    assert count_items(takewhile(lambda date: date.year < 1997, dates(1996))) == 366
    assert count_items(takewhile(lambda date: date.year < 2001, dates(2000))) == 365


def test_amicable_pairs():
    assert next(iter(amicable_pairs(10000))) == (220, 284)

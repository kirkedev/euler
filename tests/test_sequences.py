from itertools import islice

from lib.factors import is_prime, factors
from lib.sequences import primes, triangular_numbers, collatz_sequence, fibonacci


def test_primes():
    assert list(islice(primes(), 0, 10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert all(is_prime(number) for number in islice(primes(), 0, 100))


def test_triangular_numbers():
    assert list(islice(triangular_numbers(), 0, 10)) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert next(number for number in triangular_numbers() if sum(1 for _ in factors(number)) >= 5) == 28


def test_collatz_sequence():
    assert list(collatz_sequence(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_fibonacci():
    assert list(islice(fibonacci(), 5)) == [1, 2, 3, 5, 8]

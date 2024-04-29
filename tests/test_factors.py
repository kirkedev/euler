from lib.factors import is_divisible_by, is_prime, factors, prime_factors, proper_divisors


def test_is_multiple():
    is_multiple_of_three = is_divisible_by(3)
    is_multiple_of_five = is_divisible_by(5)

    assert is_multiple_of_three(1) is False
    assert is_multiple_of_three(2) is False
    assert is_multiple_of_three(3)
    assert is_multiple_of_three(6)
    assert is_multiple_of_three(9)

    assert is_multiple_of_five(1) is False
    assert is_multiple_of_five(3) is False
    assert is_multiple_of_five(5)
    assert is_multiple_of_five(10)


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert is_prime(11)
    assert not is_prime(12)
    assert is_prime(13)


def test_factors():
    assert list(factors(31)) == [1, 31]
    assert list(factors(4)) == [1, 2, 4]
    assert list(factors(8)) == [1, 2, 4, 8]
    assert list(factors(9)) == [1, 3, 9]
    assert list(factors(12)) == [1, 2, 3, 4, 6, 12]
    assert list(factors(21)) == [1, 3, 7, 21]
    assert list(factors(13195)) == [1, 5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639, 13195]


def test_prime_factors():
    assert list(prime_factors(13195)) == [5, 7, 13, 29]


def test_proper_divisors():
    assert list(proper_divisors(220)) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert list(proper_divisors(284)) == [1, 2, 4, 71, 142]

    assert sum(proper_divisors(220)) == 284
    assert sum(proper_divisors(284)) == 220

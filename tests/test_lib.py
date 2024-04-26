from itertools import islice

from lib import is_divisible_by, fibonacci, is_prime, factors, prime_factors, is_palindrome, is_palindromic_number, \
    products, squares, primes, triangular_numbers, collatz_sequence, count_edges


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


def test_fibonacci():
    assert list(islice(fibonacci(), 5)) == [1, 2, 3, 5, 8]


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


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("kayak")
    assert is_palindrome("radar")
    assert is_palindrome("A man a plan a canal panama")
    assert is_palindrome("A man, a plan, a canal -- panama!")
    assert is_palindrome("9009")
    assert not is_palindrome("Hello, World!")


def test_is_palindromic_number():
    assert not is_palindromic_number(9099)
    assert is_palindromic_number(9009)
    assert max(filter(is_palindromic_number, products(range(1, 100)))) == 9009


def test_sum_of_squares():
    assert sum(squares(range(1, 11))) == 385


def test_primes():
    assert list(islice(primes(), 0, 10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert all(is_prime(number) for number in islice(primes(), 0, 100))


def test_triangular_numbers():
    assert list(islice(triangular_numbers(), 0, 10)) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert next(number for number in triangular_numbers() if sum(1 for _ in factors(number)) >= 5) == 28


def test_collatz_sequence():
    assert list(collatz_sequence(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_count_edges():
    assert count_edges(2, 2) == 6

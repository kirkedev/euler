from lib.more_itertools import add_items
from lib.numeric import is_palindromic_number, products, squared


def test_is_palindromic_number():
    assert not is_palindromic_number(9099)
    assert is_palindromic_number(9009)
    assert max(filter(is_palindromic_number, products(range(1, 100)))) == 9009


def test_sum_of_squares():
    assert sum(squared(range(1, 11))) == 385


def test_add_lists():
    assert list(add_items([2, 4, 6], [8, 5, 9])) == [10, 9, 15]
    assert list(add_items([2, 4, 6], [5, 9, 3])) == [7, 13, 9]
    assert list(add_items([1, 2, 3], [4, 5, 6], [7, 8, 9])) == [12, 15, 18]

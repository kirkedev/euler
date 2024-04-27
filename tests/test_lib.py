from functools import reduce

from lib import is_palindrome, is_palindromic_number, count_edges, products, squared, add_items, step_triangle


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
    assert sum(squared(range(1, 11))) == 385


def test_count_edges():
    assert count_edges(2, 2) == 6


def test_add_lists():
    assert list(add_items([2, 4, 6], [8, 5, 9])) == [10, 9, 15]
    assert list(add_items([2, 4, 6], [5, 9, 3])) == [7, 13, 9]
    assert list(add_items([1, 2, 3], [4, 5, 6], [7, 8, 9])) == [12, 15, 18]


def test_step_triangle():
    triangle = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]

    assert step_triangle(triangle[3], triangle[2]) == [10, 13, 15]
    assert step_triangle([10, 13, 15], triangle[1]) == [20, 19]
    assert step_triangle([20, 19], triangle[0]) == [23]
    assert reduce(step_triangle, triangle[::-1])[0] == 23

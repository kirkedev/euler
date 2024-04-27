from lib import is_palindrome, is_palindromic_number, count_edges, products, squared


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

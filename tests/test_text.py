from lib.text import is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("kayak")
    assert is_palindrome("radar")
    assert is_palindrome("A man a plan a canal panama")
    assert is_palindrome("A man, a plan, a canal -- panama!")
    assert is_palindrome("9009")
    assert not is_palindrome("Hello, World!")

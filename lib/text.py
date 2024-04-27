import re


def is_palindrome(string: str) -> bool:
    stripped = re.sub(r"[\W\s]", "", string.lower())
    return stripped == stripped[::-1]

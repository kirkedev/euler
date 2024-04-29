import re
from string import ascii_uppercase
from typing import Iterable


def is_palindrome(string: str) -> bool:
    stripped = re.sub(r"[\W\s]", "", string.lower())
    return stripped == stripped[::-1]


def alphabetic_position(char: str) -> int:
    return ascii_uppercase.index(char) + 1


def alphabetic_positions(string: str) -> Iterable[int]:
    return map(alphabetic_position, string)

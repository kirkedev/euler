from collections import deque
from itertools import islice, chain, takewhile, dropwhile
from typing import Iterable, Iterator

from lib import T, Predicate


def drop(count: int, iterable: Iterable[T]) -> Iterator[T]:
    return islice(iterable, count, count + 1)


def take(count: int, iterable: Iterable[T]) -> Iterator[T]:
    return islice(iterable, count)


def takeuntil(predicate: Predicate[T], iterable: Iterable[T]) -> Iterable[T]:
    return takewhile(lambda item: not predicate(item), iterable)


def dropuntil(predicate: Predicate[T], iterable: Iterable[T]) -> Iterator[T]:
    return dropwhile(lambda item: not predicate(item), iterable)


def window(iterable: Iterable[T], size: int) -> Iterable[Iterable[T]]:
    iterator = iter(iterable)
    result = deque(islice(iterator, size - 1), maxlen=size)

    for item in iterator:
        result.append(item)
        yield tuple(result)


def flatten(iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    return chain(*iterable)


def count_items(iterable: Iterable[T]) -> int:
    return sum(1 for _ in iterable)


def count_if(predicate: Predicate[T], iterable: Iterable[T]) -> int:
    return sum(1 for item in iterable if predicate(item))


def count_letters(string: str) -> int:
    return sum(1 for char in string if char.isalpha())


def add_items(*iterables: Iterable[int]) -> Iterable[int]:
    return map(sum, zip(*iterables))


def max_items(*iterables: Iterable[int]) -> Iterable[int]:
    return map(max, zip(*iterables))

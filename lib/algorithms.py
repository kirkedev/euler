from functools import lru_cache
from typing import List

from lib.more_itertools import add_items, max_items


def max_step(total: List[int], row: List[int]) -> List[int]:
    return list(max_items(add_items(row, total[:-1]), add_items(row, total[1:])))


@lru_cache
def count_edges(row: int, column: int) -> int:
    return 1 if row == 0 or column == 0 else count_edges(row - 1, column) + count_edges(row, column - 1)

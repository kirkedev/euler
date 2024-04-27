from itertools import takewhile
from typing import Iterable, List, Generic

from lib import Coordinates, Direction, Dimensions, T


def vector(start: Coordinates, direction: Direction) -> Iterable[Coordinates]:
    x, y = start
    dx, dy = direction

    while True:
        yield x, y
        x += dx
        y += dy


def limit(vector: Iterable[Coordinates], dimensions: Dimensions) -> Iterable[Coordinates]:
    width, height = dimensions
    return takewhile(lambda position: 0 <= position[0] < width and 0 <= position[1] < height, vector)


def diagonals(dimensions: Dimensions) -> Iterable[List[Coordinates]]:
    width, height = dimensions

    for y in range(height):
        yield list(limit(vector((0, y), (1, 1)), dimensions))

    for x in range(1, width):
        yield list(limit(vector((x, 0), (1, 1)), dimensions))


def antidiagonals(dimensions: Dimensions) -> Iterable[List[Coordinates]]:
    width, height = dimensions

    for y in range(height):
        yield list(limit(vector((0, y), (1, -1)), dimensions))

    for x in range(1, width):
        yield list(limit(vector((x, height - 1), (1, -1)), dimensions))


class Grid(Generic[T]):
    grid: List[List[T]]

    def __init__(self, grid: List[List[T]]):
        self.grid = grid

    @property
    def height(self):
        return len(self.grid)

    @property
    def width(self):
        return len(self.grid[0])

    def rows(self) -> Iterable[List[T]]:
        return self.grid

    def columns(self) -> Iterable[List[T]]:
        return map(list, zip(*self.grid))

    def diagonals(self) -> Iterable[List[T]]:
        for diagonal in diagonals((self.width, self.height)):
            yield [self.grid[top][left] for top, left in diagonal]

    def antidiagonals(self) -> Iterable[List[T]]:
        for diagonal in antidiagonals((self.width, self.height)):
            yield [self.grid[top][left] for top, left in diagonal]

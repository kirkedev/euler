from typing import Callable, TypeVar, Tuple, TypeAlias

T = TypeVar("T")
Predicate = Callable[[T], bool]
Coordinates: TypeAlias = Tuple[int, int]
Direction: TypeAlias = Tuple[int, int]
Dimensions: TypeAlias = Tuple[int, int]

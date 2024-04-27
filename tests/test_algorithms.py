from functools import reduce

from lib.algorithms import count_edges, max_step


def test_count_edges():
    assert count_edges(2, 2) == 6


def test_step_triangle():
    triangle = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]

    assert max_step(triangle[3], triangle[2]) == [10, 13, 15]
    assert max_step([10, 13, 15], triangle[1]) == [20, 19]
    assert max_step([20, 19], triangle[0]) == [23]
    assert reduce(max_step, triangle[::-1])[0] == 23

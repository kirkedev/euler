from lib.grid import limit, vector, Grid


def test_vector():
    # diagonals
    assert list(limit(vector((2, 0), (1, 1)), (3, 3))) == [(2, 0)]
    assert list(limit(vector((1, 0), (1, 1)), (3, 3))) == [(1, 0), (2, 1)]
    assert list(limit(vector((0, 0), (1, 1)), (3, 3))) == [(0, 0), (1, 1), (2, 2)]
    assert list(limit(vector((0, 1), (1, 1)), (3, 3))) == [(0, 1), (1, 2)]
    assert list(limit(vector((0, 2), (1, 1)), (3, 3))) == [(0, 2)]

    # anti-diagonals
    assert list(limit(vector((0, 0), (-1, 1)), (3, 3))) == [(0, 0)]
    assert list(limit(vector((1, 0), (-1, 1)), (3, 3))) == [(1, 0), (0, 1)]
    assert list(limit(vector((2, 0), (-1, 1)), (3, 3))) == [(2, 0), (1, 1), (0, 2)]
    assert list(limit(vector((2, 1), (-1, 1)), (3, 3))) == [(2, 1), (1, 2)]
    assert list(limit(vector((2, 2), (-1, 1)), (3, 3))) == [(2, 2)]


def test_coordinate_vectors():
    grid = Grid([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    assert list(grid.rows()) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    assert list(grid.columns()) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

    assert list(grid.diagonals()) == [
        [1, 5, 9],
        [2, 6],
        [3],
        [4, 8],
        [7]
    ]

    assert list(grid.antidiagonals()) == [
        [1],
        [2, 4],
        [3, 5, 7],
        [6, 8],
        [9]
    ]

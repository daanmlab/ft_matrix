import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix


def test_reduced_row_echelon():
    m = Matrix(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    assert m.reduced_row_echelon() == expected

    m = Matrix(
        [
            [1.0, 2.0, -1.0, -4.0],
            [0.0, 1.0, 2.0, 3.0],
            [0.0, 0.0, 1.0, 2.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, -1.0],
            [0.0, 0.0, 1.0, 2.0],
        ]
    )
    assert m.reduced_row_echelon() == expected

    m = Matrix(
        [
            [0.0, 0.0, 0.0],
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, -1.0],
            [0.0, 1.0, 2.0],
            [0.0, 0.0, 0.0],
        ]
    )
    assert m.reduced_row_echelon() == expected

    m = Matrix(
        [
            [2.0, 0.0, 0.0],
            [3.0, 1.0, 0.0],
            [1.0, 4.0, 5.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    assert m.reduced_row_echelon() == expected

    m = Matrix(
        [
            [1.0, 2.0, 3.0],
            [0.0, 0.0, 0.0],
            [4.0, 5.0, 6.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, -1.0],
            [0.0, 1.0, 2.0],
            [0.0, 0.0, 0.0],
        ]
    )
    assert m.reduced_row_echelon() == expected


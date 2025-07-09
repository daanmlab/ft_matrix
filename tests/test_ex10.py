import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix

def test_row_echelon():
    m = Matrix(
        [
            [1.0, 2.0, -1.0, -4.0],
            [0.0, 1.0, 2.0, 3.0],
            [0.0, 0.0, 1.0, 2.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 2.0, -1.0, -4.0],
            [0.0, 1.0, 2.0, 3.0],
            [0.0, 0.0, 1.0, 2.0],
        ]
    )
    assert m.row_echelon()[0] == expected, f"{m.row_echelon()[0]}"

    m = Matrix(
        [
            [0.0, 0.0, 0.0],
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 2.0, 3.0],
            [0.0, -3.0, -6.0],
            [0.0, 0.0, 0.0],
        ]
    )
    assert m.row_echelon()[0] == expected, f"{m.row_echelon()[0]}"

    m = Matrix(
        [
            [2.0, 0.0, 0.0],
            [3.0, 1.0, 0.0],
            [1.0, 4.0, 5.0],
        ]
    )
    expected = Matrix(
        [
            [2.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 5.0],
        ]
    )
    assert m.row_echelon()[0] == expected, f"{m.row_echelon()[0]}"

def test_reduced_row_echelon_zero_matrix():
    m = Matrix(
        [
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
    )
    expected = Matrix(
        [
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
    )
    assert m.reduced_row_echelon() == expected, f"{m.reduced_row_echelon()}"

def test_reduced_row_echelon_single_row():
    m = Matrix([[2.0, 4.0, 6.0]])
    expected = Matrix([[1.0, 2.0, 3.0]])
    assert m.reduced_row_echelon() == expected

def test_reduced_row_echelon_single_column():
    m = Matrix([[2.0], [4.0], [6.0]])
    expected = Matrix([[1.0], [0.0], [0.0]])
    assert m.reduced_row_echelon() == expected, f"{m.reduced_row_echelon()}"

def test_reduced_row_echelon_already_rref():
    m = Matrix(
        [
            [1.0, 0.0, 0.0, 2.0],
            [0.0, 1.0, 0.0, 3.0],
            [0.0, 0.0, 1.0, 4.0],
        ]
    )
    expected = Matrix(
        [
            [1.0, 0.0, 0.0, 2.0],
            [0.0, 1.0, 0.0, 3.0],
            [0.0, 0.0, 1.0, 4.0],
        ]
    )
    assert m.reduced_row_echelon() == expected

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


from utils.Matrix import Matrix



def test_identity_matrix():
    m = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    expected = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    assert m.reduced_row_echelon() == expected


def test_full_rank():
    m = Matrix([
        [1.0, 2.0, -1.0, -4.0],
        [0.0, 1.0, 2.0, 3.0],
        [0.0, 0.0, 1.0, 2.0],
    ])
    expected = Matrix([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, -1.0],
        [0.0, 0.0, 1.0, 2.0],
    ])
    assert m.reduced_row_echelon() == expected


def test_requires_row_swap():
    m = Matrix([
        [0.0, 0.0, 0.0],
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ])
    expected = Matrix([
        [1.0, 0.0, -1.0],
        [0.0, 1.0, 2.0],
        [0.0, 0.0, 0.0],
    ])
    assert m.reduced_row_echelon() == expected


def test_lower_triangular():
    m = Matrix([
        [2.0, 0.0, 0.0],
        [3.0, 1.0, 0.0],
        [1.0, 4.0, 5.0],
    ])
    expected = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    assert m.reduced_row_echelon() == expected


def test_zero_row():
    m = Matrix([
        [1.0, 2.0, 3.0],
        [0.0, 0.0, 0.0],
        [4.0, 5.0, 6.0],
    ])
    expected = Matrix([
        [1.0, 0.0, -1.0],
        [0.0, 1.0, 2.0],
        [0.0, 0.0, 0.0],
    ])
    assert m.reduced_row_echelon() == expected


def ex10():
    test_identity_matrix()
    test_full_rank()
    test_requires_row_swap()
    test_lower_triangular()
    test_zero_row()
    print("All tests passed!")

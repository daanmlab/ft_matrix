import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix


def test_inverse():
    m = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    assert m.inverse() == Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    m = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    assert m.inverse() == Matrix([[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]])

    m = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    expected = Matrix(
        [
            [0.649425287, 0.097701149, -0.655172414],
            [-0.781609195, -0.126436782, 0.965517241],
            [0.143678161, 0.074712644, -0.206896552],
        ]
    )
    inv = m.inverse()
    for r1, r2 in zip(inv.data, expected.data):
        for a, b in zip(r1, r2):
            assert math.isclose(a, b, rel_tol=1e-6)


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix


def test_trace():
    u = Matrix(data=[[1.0, 0.0], [0.0, 1.0]])
    assert u.trace() == 2.0

    u = Matrix(data=[[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    assert u.trace() == 9.0

    u = Matrix(data=[[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
    assert u.trace() == -21.0


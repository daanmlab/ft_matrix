import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix


def test_transpose():
    m = Matrix(data=[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    trans = m.transpose()
    assert trans == Matrix(data=[[1.0, 3.0, 5.0], [2.0, 4.0, 6.0]])
    assert trans.transpose() == m


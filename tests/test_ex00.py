import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector
from utils.Matrix import Matrix


def test_vector_operations():
    u = Vector(data=[2.0, 3.0])
    v = Vector(data=[5.0, 7.0])
    assert u.add(v).data == [7.0, 10.0]

    u = Vector(data=[2.0, 3.0])
    v = Vector(data=[5.0, 7.0])
    assert u.sub(v).data == [-3.0, -4.0]

    u = Vector(data=[2.0, 3.0])
    assert u.scl(2.0).data == [4.0, 6.0]


def test_matrix_operations():
    u = Matrix(data=[[1.0, 2.0], [3.0, 4.0]])
    v = Matrix(data=[[7.0, 4.0], [-2.0, 2.0]])
    assert u.add(v) == Matrix(data=[[8.0, 6.0], [1.0, 6.0]])

    u = Matrix(data=[[1.0, 2.0], [3.0, 4.0]])
    v = Matrix(data=[[7.0, 4.0], [-2.0, 2.0]])
    assert u.sub(v) == Matrix(data=[[-6.0, -2.0], [5.0, 2.0]])

    u = Matrix(data=[[1.0, 2.0], [3.0, 4.0]])
    assert u.scl(2.0) == Matrix(data=[[2.0, 4.0], [6.0, 8.0]])


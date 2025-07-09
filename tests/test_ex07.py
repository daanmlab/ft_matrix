import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Matrix import Matrix
from utils.Vector import Vector


def test_matrix_mul():
    u = Matrix(data=[[1.0, 0.0], [0.0, 1.0]])
    v = Vector(data=[4.0, 2.0])
    assert u.mul_vec(v) == Vector(data=[4.0, 2.0])

    u = Matrix(data=[[2.0, 0.0], [0.0, 2.0]])
    v = Vector(data=[4.0, 2.0])
    assert u.mul_vec(v) == Vector(data=[8.0, 4.0])

    u = Matrix(data=[[2.0, -2.0], [-2.0, 2.0]])
    v = Vector(data=[4.0, 2.0])
    assert u.mul_vec(v) == Vector(data=[4.0, -4.0])

    u = Matrix(data=[[1.0, 0.0], [0.0, 1.0]])
    m = Matrix(data=[[1.0, 0.0], [0.0, 1.0]])
    assert u.mul_mat(m) == Matrix(data=[[1.0, 0.0], [0.0, 1.0]])

    u = Matrix(data=[[1.0, 0.0], [0.0, 1.0]])
    m = Matrix(data=[[2.0, 1.0], [4.0, 2.0]])
    assert u.mul_mat(m) == Matrix(data=[[2.0, 1.0], [4.0, 2.0]])

    u = Matrix(data=[[3.0, -5.0], [6.0, 8.0]])
    m = Matrix(data=[[2.0, 1.0], [4.0, 2.0]])
    assert u.mul_mat(m) == Matrix(data=[[-14.0, -7.0], [44.0, 22.0]])


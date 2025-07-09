import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector
from utils.Matrix import Matrix
from utils.funcs import lerp


def test_lerp():
    assert lerp(0.0, 1.0, 0.0) == 0.0
    assert lerp(0.0, 1.0, 1.0) == 1.0
    assert lerp(0.0, 1.0, 0.5) == 0.5
    assert math.isclose(lerp(21.0, 42.0, 0.3), 27.3)

    v = Vector(data=[2.0, 1.0])
    u = Vector(data=[4.0, 2.0])
    result = lerp(v, u, 0.3)
    assert all(math.isclose(a, b) for a, b in zip(result.data, [2.6, 1.3]))

    m1 = Matrix(data=[[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix(data=[[20.0, 10.0], [30.0, 40.0]])
    result = lerp(m1, m2, 0.5)
    assert result == Matrix(data=[[11.0, 5.5], [16.5, 22.0]])


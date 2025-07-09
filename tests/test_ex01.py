import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector
from utils.funcs import linear_combination


def test_linear_combination():
    e1 = Vector(data=[1.0, 0.0, 0.0])
    e2 = Vector(data=[0.0, 1.0, 0.0])
    e3 = Vector(data=[0.0, 0.0, 1.0])
    result = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
    assert result.data == [10.0, -2.0, 0.5]

    v1 = Vector(data=[1.0, 2.0, 3.0])
    v2 = Vector(data=[0.0, 10.0, -100.0])
    result = linear_combination([v1, v2], [10.0, -2.0])
    assert result.data == [10.0, 0.0, 230.0]


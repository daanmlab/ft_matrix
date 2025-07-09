import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector
from utils.funcs import angle_cos


def test_angle_cos():
    u = Vector(data=[1.0, 0.0])
    v = Vector(data=[1.0, 0.0])
    assert math.isclose(angle_cos(u, v), 1.0)

    u = Vector(data=[1.0, 0.0])
    v = Vector(data=[0.0, 1.0])
    assert math.isclose(angle_cos(u, v), 0.0)

    u = Vector(data=[-1.0, 1.0])
    v = Vector(data=[1.0, -1.0])
    assert math.isclose(angle_cos(u, v), -1.0)

    u = Vector(data=[2.0, 1.0])
    v = Vector(data=[4.0, 2.0])
    assert math.isclose(angle_cos(u, v), 1.0)

    u = Vector(data=[1.0, 2.0, 3.0])
    v = Vector(data=[4.0, 5.0, 6.0])
    assert math.isclose(angle_cos(u, v), 0.974631846, rel_tol=1e-6)


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector


def test_dot_product():
    u = Vector(data=[0.0, 0.0])
    v = Vector(data=[1.0, 1.0])
    assert u.dot(v) == 0.0

    u = Vector(data=[1.0, 1.0])
    v = Vector(data=[1.0, 1.0])
    assert u.dot(v) == 2.0

    u = Vector(data=[-1.0, 6.0])
    v = Vector(data=[3.0, 2.0])
    assert u.dot(v) == 9.0


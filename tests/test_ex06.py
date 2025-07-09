import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector
from utils.funcs import cross_product


def test_cross_product():
    u = Vector(data=[0.0, 0.0, 1.0])
    v = Vector(data=[1.0, 0.0, 0.0])
    assert cross_product(u, v).data == [0.0, 1.0, 0.0]

    u = Vector(data=[1.0, 2.0, 3.0])
    v = Vector(data=[4.0, 5.0, 6.0])
    assert cross_product(u, v).data == [-3.0, 6.0, -3.0]

    u = Vector(data=[4.0, 2.0, -3.0])
    v = Vector(data=[-2.0, -5.0, 16.0])
    assert cross_product(u, v).data == [17.0, -58.0, -16.0]


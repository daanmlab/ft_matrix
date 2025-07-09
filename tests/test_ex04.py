import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.Vector import Vector


def test_norms():
    u = Vector(data=[0.0, 0.0, 0.0])
    assert u.norm_1() == 0.0
    assert u.norm() == 0.0
    assert u.norm_inf() == 0.0

    u = Vector(data=[1.0, 2.0, 3.0])
    assert u.norm_1() == 6.0
    assert math.isclose(u.norm(), 3.74165738, rel_tol=1e-7)
    assert u.norm_inf() == 3.0

    u = Vector(data=[-1.0, -2.0])
    assert u.norm_1() == 3.0
    assert math.isclose(u.norm(), 2.236067977, rel_tol=1e-7)
    assert u.norm_inf() == 2.0


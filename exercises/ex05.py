from utils.Vector import Vector
from utils.funcs import angle_cos


def ex05():
    v = Vector(data=[1, 2, 3])
    u = Vector(data=[4, 5, 6])

    print(f"{angle_cos(v, u)=}")

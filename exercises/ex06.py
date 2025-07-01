from utils.Vector import Vector
from utils.funcs import cross_product


def ex06():
    v = Vector(data=[1, 2, 3])
    u = Vector(data=[4, 5, 6])

    print(f"{cross_product(v, u)=}")

from utils.Matrix import Matrix
from utils.Vector import Vector
from utils.funcs import lerp


def ex02():
    v = Vector(data=[2, 5])
    u = Vector(data=[-1, 4])
    for i in range(100):
        i = round(i * 0.01, 2)
        print(f"(t: {i}) | ", lerp(v, u, i))

    m1 = Matrix(
        data=[
            [2, 5],
            [-1, 4],
        ]
    )
    m2 = Matrix(
        data=[
            [-1, 4],
            [2, 5],
        ]
    )
    for i in range(100):
        i = round(i * 0.01, 2)
        print(f"(t: {i}) | ", lerp(m1, m2, i))



from utils import Vector, linear_combination


def ex01():
    vectors: list[Vector[float]] = [
        Vector(data=[1, 0, 0]),
        Vector(data=[0, 1, 0]),
        Vector(data=[0, 0, 1]),
    ]
    coefficients: list[float] = [
        3, -5, 9
    ]
    print("vectors      : ", vectors)
    print("coefficients : ", coefficients)
    print("result       : ", linear_combination(vectors, coefficients))
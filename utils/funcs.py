from typing import TypeVar

from utils.Matrix import Matrix
from utils.Vector import Vector
from utils.constants import T


K = TypeVar("K", Vector, Matrix)


def lerp(v: K, u: K, t: T) -> K:
    return (v * t) + (u * (1 - t))


def linear_combination(vectors: list[Vector[T]], coefficients: list[T]) -> Vector[T]:
    """
    Computes the linear combination of a list of vectors with given coefficients.
    """
    if len(vectors) == 0:
        raise ValueError("No vectors provided")
    if len(vectors) != len(coefficients):
        raise ValueError("Number of vectors and coefficients must match")
    length = len(vectors[0])
    for v in vectors:
        if len(v) != length:
            raise ValueError("All vectors must be of the same length")
    result_data: list[T] = [
        sum(vectors[j][i] * coefficients[j] for j in range(len(vectors)))  # type: ignore
        for i in range(length)
    ]
    return Vector(data=result_data)

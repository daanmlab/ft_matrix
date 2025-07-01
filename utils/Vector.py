from math import sqrt
from typing import Generic
from pydantic import BaseModel

from utils.constants import T


class Vector(BaseModel, Generic[T]):
    """
    A simple vector class that holds a list of T.
    """

    data: list[T]

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, index: int) -> T:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)

    def __add__(self, other: "Vector[T]") -> "Vector[T]":
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length to add")
        return Vector[T](data=[self[i] + other[i] for i in range(len(self))])  # type: ignore

    def add(self, other: "Vector[T]") -> "Vector[T]":
        """
        Adds another vector to this vector.
        """
        self.data = (self + other).data
        return self

    def __sub__(self, other: "Vector[T]") -> "Vector[T]":
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length to subtract")
        return Vector[T](data=[self[i] - other[i] for i in range(len(self))])  # type: ignore

    def sub(self, other: "Vector[T]") -> "Vector[T]":
        """
        Subtracts another vector from this vector.
        """
        self.data = (self - other).data
        return self

    def __mul__(self, scalar: T) -> "Vector[T]":
        """
        Multiplies this vector by a scalar.
        """
        return Vector[T](data=[x * scalar for x in self.data])  # type: ignore

    def scl(self, scalar: T) -> "Vector[T]":
        """
        Scales this vector by a scalar.
        """
        self.data = (self * scalar).data
        return self

    def dot(self, v: "Vector[T]") -> T:
        if len(self) != len(v):
            raise ValueError(
                "Vectors must be of the same length to get the dot product"
            )
        return sum([(self[i] * v[i]) for i in range(len(self))])

    def norm_1(self) -> float:
        return sum([abs(x) for x in self.data])

    def norm(self, n: T = 2) -> float:
        return sqrt(sum([pow(abs(x), n) for x in self.data]))

    def norm_inf(self) -> float:
        return max([abs(x) for x in self.data])

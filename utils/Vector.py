from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")

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
        return Vector[T](data=[self[i] + other[i] for i in range(len(self))]) # type: ignore

    def add(self, other: "Vector[T]") -> "Vector[T]":
        """
        Adds another vector to this vector.
        """
        self.data = (self + other).data
        return self

    def __sub__(self, other: "Vector[T]") -> "Vector[T]":
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length to subtract")
        return Vector[T](data=[self[i] - other[i] for i in range(len(self))]) # type: ignore

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
        return Vector[T](data=[x * scalar for x in self.data]) # type: ignore

    def scl(self, scalar: T) -> "Vector[T]":
        """
        Scales this vector by a scalar.
        """
        self.data = (self * scalar).data
        return self
    
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
    result_data = [
        sum(vectors[j][i] * coefficients[j] for j in range(len(vectors))) # type: ignore
        for i in range(length)
    ]
    return Vector(data=result_data)
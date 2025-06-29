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
        return self + other
    
    def __sub__(self, other: "Vector[T]") -> "Vector[T]":
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length to subtract")
        return Vector[T](data=[self[i] - other[i] for i in range(len(self))]) # type: ignore

    def sub(self, other: "Vector[T]") -> "Vector[T]":
        """
        Subtracts another vector from this vector.
        """
        return self - other
    
    def __mul__(self, scalar: T) -> "Vector[T]":
        """
        Multiplies this vector by a scalar.
        """
        return Vector[T](data=[x * scalar for x in self.data]) # type: ignore

    def mul(self, scalar: T) -> "Vector[T]":
        """
        Multiplies this vector by a scalar.
        """
        return self * scalar
from typing import Generic, cast
from pydantic import BaseModel

from utils.Vector import Vector
from utils.constants import T


class Matrix(BaseModel, Generic[T]):
    """
    A simple matrix class that holds a list of lists of T.
    """

    data: list[list[T]]

    def __init__(self, data: list[list[T]]):
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Data must be a list of lists")
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")
        super().__init__(data=data)

    def __str__(self) -> str:
        return f"""[
\t{"\n\t".join([" ".join([
    f"{col}" for col in row
]) for row in self.data])}
]"""

    def __getitem__(self, index: int) -> list[T]:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)

    def __add__(self, other: "Matrix[T]") -> "Matrix[T]":
        if len(self) != len(other) or len(self[0]) != len(other[0]):
            raise ValueError("Matrices must be of the same dimensions to add")
        return Matrix[T](data=[[self[i][j] + other[i][j] for j in range(len(self[0]))] for i in range(len(self))])  # type: ignore

    def add(self, other: "Matrix[T]") -> "Matrix[T]":
        """
        Adds another matrix to this matrix.
        """
        self.data = (self + other).data
        return self

    def __sub__(self, other: "Matrix[T]") -> "Matrix[T]":
        if len(self) != len(other) or len(self[0]) != len(other[0]):
            raise ValueError("Matrices must be of the same dimensions to subtract")
        return Matrix(data=[[self[i][j] - other[i][j] for j in range(len(self[0]))] for i in range(len(self))])

    def sub(self, other: "Matrix[T]") -> "Matrix[T]":
        """
        Subtracts another matrix from this matrix.
        """
        self.data = (self - other).data
        return self

    def __mul__(self, scalar: T) -> "Matrix[T]":
        """
        Multiplies this matrix by a scalar.
        """
        return Matrix[T](data=[[x * scalar for x in row] for row in self.data])  # type: ignore

    def scl(self, scalar: T) -> "Matrix[T]":
        """
        Scales this matrix by a scalar.
        """
        self.data = (self * scalar).data
        return self

    def to_vectors(self) -> list[Vector[T]]:
        vector_size = len(self.data)
        _data = sum(self.data, [])
        step = len(_data) // vector_size
        return [Vector(data=_data[i::step]) for i in range(step)]

    @classmethod
    def from_vectors(cls, vectors: list[Vector[T]]) -> "Matrix[T]":
        v_size = len(vectors[0])
        if any([(len(v) != v_size) for v in vectors]):
            raise ValueError("Not all vectors are the same size")
        return cls(
            data=[[v[i] for v in vectors] for i in range(v_size)],
        )

    def mul_vec(self: "Matrix[T]", v: Vector[T], raises=True) -> Vector[T]:
        if raises and len(self) < len(v):
            raise ValueError("Vector can't have more dimensions than matrix")
        mat: list[Vector[T]] = self.to_vectors()
        return sum(
            [(col * v[i]) for i, col in enumerate(mat)],
            Vector(data=[cast(T, 0)] * len(self)),
        )

    def mul_mat(self: "Matrix[T]", m: "Matrix[T]") -> "Matrix[T]":
        return Matrix.from_vectors([
            self.mul_vec(v, raises=False) for v in m.to_vectors()
        ])
    
    def trace(self) -> T:
        if ((size := len(self)) != len(self.data[0])):
            raise ValueError("Cannot get trace of non square matrix")
        return sum([self.data[i][i] for i in range(size)], cast(T, 0))

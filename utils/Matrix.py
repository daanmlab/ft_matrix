from typing import Generic, Literal, cast
from pydantic import BaseModel

from utils.Vector import Vector
from utils.constants import T


class Coords(BaseModel):
    y: int
    x: int


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
    f"{float(cast(float, col))}" for col in row
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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        if len(self) != len(other) or len(self[0]) != len(other[0]):
            return False
        for i in range(len(self)):
            for j in range(len(self[0])):
                if self[i][j] != other[i][j]:
                    return False
        return True

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

    def to_rows_as_vectors(self) -> list[Vector[T]]:
        return [Vector(data=x) for x in self.data]

    @classmethod
    def from_vectors(cls, vectors: list[Vector[T]]) -> "Matrix[T]":
        v_size = len(vectors[0])
        if any([(len(v) != v_size) for v in vectors]):
            raise ValueError("Not all vectors are the same size")
        return cls(
            data=[[v[i] for v in vectors] for i in range(v_size)],
        )

    @classmethod
    def from_rows_as_vectors(cls, vectors: list[Vector[T]]) -> "Matrix[T]":
        v_size = len(vectors[0])
        if any([(len(v) != v_size) for v in vectors]):
            raise ValueError("Not all vectors are the same size")
        return cls(
            data=[x.data for x in vectors],
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
        return Matrix.from_vectors([self.mul_vec(v, raises=False) for v in m.to_vectors()])

    def trace(self) -> T:
        if (size := len(self)) != len(self.data[0]):
            raise ValueError("Cannot get trace of non square matrix")
        return sum([self.data[i][i] for i in range(size)], cast(T, 0))

    def transpose(self) -> "Matrix[T]":
        return Matrix(data=[v.data for v in self.to_vectors()])

    def reduced_row_echelon(self) -> "Matrix[T]":
        # Gauss-Jordan elimination
        A = self.copy(deep=True).to_rows_as_vectors()
        pivot_columns = []


        def find_pivot(y=0, x=0) -> Coords | Literal[False]:
            for _x in range(x, len(A[0])):
                for _y in range(y, len(A)):
                    if A[_y][_x] != 0:
                        return Coords(y=_y, x=_x)
            return False
        def swap_rows(i: int, j: int):
            A[i], A[j] = A[j], A[i]

        # Forward phase (REF)
        for y in range(len(A)):
            c = find_pivot(y=y)
            if c is False:
                continue
            swap_rows(c.y, y)
            pivot_columns.append(c.x)

            # Normalize current row
            pivot_value = A[y][c.x]
            for x in range(c.x, len(A[y])):
                A[y][x] = cast(T, A[y][x] / pivot_value)

            # Eliminate below
            for r in range(y + 1, len(A)):
                factor = A[r][c.x]
                A[r] -= A[y] * factor


        # Backward phase (RREF)
        for y in range(len(A) - 1, -1, -1):
            # Find pivot
            if y >= len(pivot_columns):
                continue
            p = pivot_columns[y]

            # Eliminate above
            for y_i in range(y - 1, -1, -1):
                factor = A[y_i][p]
                A[y_i] -= A[y] * factor


        return Matrix.from_rows_as_vectors(A)

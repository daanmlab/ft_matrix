from typing import Generic, cast
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

    def row_echelon(self) -> tuple["Matrix[T]", T]:
        # Gaussian elimination
        A = self.copy(deep=True).to_rows_as_vectors()
        rows, cols = len(A), len(A[0])
        sign: T = cast(T, 1)

        for i in range(min(rows, cols)):
            if A[i][i] == 0: # find row to swap if necesary
                for j in range(i + 1, rows):
                    if A[j][i] != 0:
                        A[j], A[i] = A[i], A[j]
                        sign *= -1
                        break
            if A[i][i] == 0: # if still zero, skip this row
                continue

            for j in range(i + 1, rows): # eliminate all rows underneath
                factor: T = cast(T, A[j][i] / A[i][i])
                A[j] -= A[i] * factor

        return (Matrix.from_rows_as_vectors(A), sign)

    def reduced_row_echelon(self) -> "Matrix[T]":
        # Gauss-Jordan elimination
        A = self.row_echelon()[0].to_rows_as_vectors()
        rows, cols = len(A), len(A[0])

        # Work from bottom to top
        for i in reversed(range(rows)):
            # Find pivot (first non-zero in row i)
            row = A[i]
            pivot_col = None
            for j in range(cols):
                if row[j] != 0:
                    pivot_col = j
                    break

            if pivot_col is None:
                continue  # skip all-zero row

            # Normalize the pivot to 1
            pivot_val = A[i][pivot_col]
            A[i] *= cast(T, 1 / pivot_val)

            # Eliminate above
            for k in range(i):
                factor = A[k][pivot_col]
                A[k] -= A[i] * factor

        return Matrix.from_rows_as_vectors(A)

    def det(self) -> T:
        (A, det) = self.row_echelon()

        for i in range(len(A)):
            det *= A[i][i]

        return det
    
    def identity(self) ->  "Matrix[T]":
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix not square")
        n = len(self.data)
        m = Matrix[T](data=
            [[cast(T, 0)] * n]*n
        )
        for i in range(n):
            m.data[i][i] = cast(T, 1)
        return m

    def inverse(self) -> "Matrix[T]":
        aug = self.copy(deep=True)
        id = self.identity()
        n = len(self.data)

        for i in range(n):
            aug.data[i] += id.data[i]

        rref = aug.reduced_row_echelon()

        for i in range(n):
            rref.data[i] = rref.data[i][n:]
        
        return rref
    
    def rank(self) -> int:
        (A, _s) = self.row_echelon()
        n = min(len(A.data[0]),len(A.data))

        for i in range(n):
            if (all([x == 0 for x in A.data[i]])):
                return i
        return n



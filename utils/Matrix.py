from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")

class Matrix(BaseModel, Generic[T]):
    """
    A simple matrix class that holds a list of lists of T.
    It inherits from BaseModel to leverage Pydantic's data validation and serialization.
    """
    data: list[list[T]]

    def __getitem__(self, index: int) -> list[T]:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f"Matrix(data={self.data})"


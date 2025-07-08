from utils.Matrix import Matrix


def ex12():
    A = Matrix(
        data=[
            [2, 1, 1],
            [1, 3, 2],
            [1, 0, 0],
        ]
    )

    print(A.inverse())

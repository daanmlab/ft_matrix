from utils.Matrix import Matrix


def ex07():
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])
    B = Matrix([
        [7, 8],
        [9, 10],
        [11, 12],
    ])

    print(A)

    print(B)

    print(A.mul_mat(B))

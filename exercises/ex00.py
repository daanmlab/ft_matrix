from utils.Matrix import Matrix
from utils.Vector import Vector


def ex00():
    u = Vector[float](data=[2.0, 3.0])
    v = Vector[float](data=[5.0, 7.0])
    u.add(v)
    print(u)
    # [7.0]
    # [10.0]

    u = Vector[float](data=[2.0, 3.0])
    v = Vector[float](data=[5.0, 7.0])
    u.sub(v)
    print(u)
    # [-3.0]
    # [-4.0]

    u = Vector[float](data=[2.0, 3.0])
    u.scl(2.0)
    print(u)
    # [4.0]
    # [6.0]

    u = Matrix[float](data=[[1.0, 2.0], [3.0, 4.0]])
    v = Matrix[float](data=[[7.0, 4.0], [-2.0, 2.0]])
    u.add(v)
    print(u)
    # [8.0, 6.0]
    # [1.0, 6.0]

    u = Matrix[float](data=[[1.0, 2.0], [3.0, 4.0]])
    v = Matrix[float](data=[[7.0, 4.0], [-2.0, 2.0]])
    u.sub(v)
    print(u)
    # [-6.0, -2.0]
    # [5.0, 2.0]

    u = Matrix[float](data=[[1.0, 2.0], [3.0, 4.0]])
    u.scl(2.0)
    print(u)
    # [2.0, 4.0]
    # [6.0, 8.0]

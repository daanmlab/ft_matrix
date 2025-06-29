from utils import Matrix, Vector

def ex00():
    u = Vector[float](data=[2., 3.])
    v = Vector[float](data=[5., 7.])
    u.add(v)
    print(u)
    # [7.0]
    # [10.0]

    u = Vector[float](data=[2., 3.])
    v = Vector[float](data=[5., 7.])
    u.sub(v)
    print(u)
    # [-3.0]
    # [-4.0]

    u = Vector[float](data=[2., 3.])
    u.scl(2.)
    print(u)
    # [4.0]
    # [6.0]

    u = Matrix[float](data=[[1., 2.], [3., 4.]])
    v = Matrix[float](data=[[7., 4.], [-2., 2.]])
    u.add(v)
    print(u)
    # [8.0, 6.0]
    # [1.0, 6.0]

    u = Matrix[float](data=[[1., 2.], [3., 4.]])
    v = Matrix[float](data=[[7., 4.], [-2., 2.]])
    u.sub(v)
    print(u)
    # [-6.0, -2.0]
    # [5.0, 2.0]

    u = Matrix[float](data=[[1., 2.], [3., 4.]])
    u.scl(2.)
    print(u)
    # [2.0, 4.0]
    # [6.0, 8.0]
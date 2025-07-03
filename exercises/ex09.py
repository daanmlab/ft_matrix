from utils.Matrix import Matrix


def ex09():
  m = Matrix(data=[
    [1,2],
    [3,4],
    [5,6],
  ])

  print(m.transpose())
  print(m.transpose().transpose())
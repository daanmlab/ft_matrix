

from utils.Vector import Vector


def ex04():
  v = Vector(data=[1, 2, 3])
  print(f"{v.norm_1()=}")
  print(f"{v.norm()=}")
  print(f"{v.norm_inf()=}")
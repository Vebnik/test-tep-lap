

class Work:
  def __init__(self, a: int, b: int) -> None:
    self.a = a; self.b = b

  @property
  def b(self):
    return self.__b

  @property
  def a(self):
    return self.__a

  @a.setter
  def a(self, value: int):
    if not isinstance(value, int):
      raise TypeError('value must be type int')
    self.__a = value

  @a.setter
  def b(self, value: int):
    if not isinstance(value, int):
      raise TypeError('value must be type int')
    self.__b = value

  def my_sum(self) -> int|float:
    return self.a + self.b

  def __str__(self) -> str:
    return f'{self.a=} {self.b=}'


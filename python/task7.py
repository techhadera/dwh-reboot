class Animal:
  instances_count = 0

  def __init__(self) -> None:
    Animal.instances_count += 1

  def voice(self):
    pass

  def get_instances_count():
    return Animal.instances_count
  get_instances_count = staticmethod(get_instances_count)

class Crab(Animal):
  def __init__(self) -> None:
    super().__init__()

  def voice(self):
    print('Clack')

class Cow(Animal):
  def __init__(self) -> None:
    super().__init__()

  def voice(self):
    print('Moo')

class Pig(Animal):
  def __init__(self) -> None:
    super().__init__()

  def voice(self):
    print('Oink')


crab = Crab()
cow = Cow()
pig = Pig()

print(Animal.get_instances_count())
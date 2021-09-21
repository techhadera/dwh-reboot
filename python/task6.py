class Animal:
  def voice(self):
    pass

class Crab(Animal):
  def voice(self):
    print('Clack')

class Cow(Animal):
  def voice(self):
    print('Moo')

class Pig(Animal):
  def voice(self):
    print('Oink')


crab = Crab()
crab.voice()

cow = Cow()
cow.voice()

pig = Pig()
pig.voice()
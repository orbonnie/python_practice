class Dog:
  def __init__(self, name):
    self.name = name
    self.tricks = []

  def add_trick(self, trick):
    self.tricks.append(trick)

  def perform(self, trick):
    if trick in self.tricks:
      print(f'{self.name} performs {trick}!')
    else:
      print(f'{self.name} doesn\'t know {trick}')

maple = Dog('Maple')
maple.add_trick('sit')
maple.add_trick('stay')
maple.add_trick('lay')

maple.perform('sit')
maple.perform('down')
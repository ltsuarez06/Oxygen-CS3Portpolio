class Hero:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

  def take_damage(self, amount):
    self.health -= amount

arthur = Hero("Arthur", 100)
arthur.take_damage(10)
print(arthur.hp)  


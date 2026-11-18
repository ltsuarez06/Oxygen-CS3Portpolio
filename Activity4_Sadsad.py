class HealthPotion:
    def restore(self):
        print("You restore 50 HP.")

class ManaPotion:
    def restore(self):
        print("You restore 30 MP.")

class speedboost:
    def restore(self):
        print("Your speed increases for 10 seconds!")

potions = [HealthPotion(), ManaPotion(), speedboost()]

health_potion = HealthPotion()
mana_potion = ManaPotion()
speed_boost = speedboost()

health1 = health_potion.restore()
mana1 = mana_potion.restore()
speed1 = speed_boost.restore()
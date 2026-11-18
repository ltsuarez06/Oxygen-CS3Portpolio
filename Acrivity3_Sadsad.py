class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
     def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

    for character in character:
            perform_move(character)

            character_list = [warrior1, mage1, archer1]


warrior1 = Warrior()
mage1 = Mage()  
archer1 = Archer()

warrior1.special_move() 
mage1.special_move()     
archer1.special_move()  

  
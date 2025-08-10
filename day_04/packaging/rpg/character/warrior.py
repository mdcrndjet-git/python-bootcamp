from .character import Character

class Warrior(Character):
    def __init__(self,name="NPC",health=10,defense=10,strength=10):
        super().__init__(name,health,defense)
        self.strength = strength

    def attack(self,other):
        damage = self.strength -other.defense
        self.health = damage

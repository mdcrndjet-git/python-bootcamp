from .character import Character

class Mage(Character):
    def __init__(self,name="NPC",health=10,defense=10,magic=10):
        super().__init__(name,health,defense)
        self.magic = magic

    def attack(self,other):
        damage = self.magic -other.defense
        self.health = damage

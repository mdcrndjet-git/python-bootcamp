from .character import Character

class Knight(Character):
    def attack(self,other):
        damage = self.defense -other.defense
        self.health = damage

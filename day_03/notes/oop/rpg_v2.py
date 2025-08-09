from abc import ABC,abstractmethod

class Character(ABC):
    def __init__(self,name="NPC",health=10,defense=10):
        self.name = name
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self,other):
        raise NotImplementedError()

    def show_health(self):
        print(f"{self.name} Health = {self.health}")

class Knight(Character):
    def attack(self,other):
        damage = self.defense -other.defense
        self.health = damage

class Mage(Character):
    def __init__(self,name="NPC",health=10,defense=10,magic=10):
        super().__init__(name,health,defense)
        self.magic = magic

    def attack(self,other):
        damage = self.magic -other.defense
        self.health = damage

class Warrior(Character):
    def __init__(self,name="NPC",health=10,defense=10,strength=10):
        super().__init__(name,health,defense)
        self.strength = strength

    def attack(self,other):
        damage = self.strength -other.defense
        self.health = damage

Knight_1 = Knight("Knight 1",health=1000,defense=1000)
Knight_1.show_health()

Knight_2 = Knight("Knight 2",health=100,defense=100)
Knight_1.show_health()

print(f"{Knight_1.name} attacks {Knight_2.name}")
Knight_2.attack(Knight_1)
Knight_1.show_health()
Knight_2.show_health()

Mage_1 = Mage("Mage 1",health=100,defense=100,magic=100)
Mage_1.attack(Knight_1)
Knight_1.show_health()
Mage_1.show_health()

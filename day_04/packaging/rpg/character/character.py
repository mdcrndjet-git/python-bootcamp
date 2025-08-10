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

from character.knight import Knight
from character.mage import Mage
from character.warrior import Warrior

Knight_1 = Knight("Knight 1",health=1000,defense=1000)
Knight_1.show_health()

Knight_2 = Knight("Knight 2",health=100,defense=100)
Knight_2.show_health()

print(f"{Knight_1.name} attacks {Knight_2.name}")

Knight_2.attack(Knight_1)
Knight_1.show_health()
Knight_2.show_health()

Mage_1 = Mage("Mage 1",health=100,defense=100,magic=100)
Mage_1.attack(Knight_1)
Knight_1.show_health()
Mage_1.show_health()

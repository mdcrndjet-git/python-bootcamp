class Candy:
    def __init__(self, flavor):
        self.flavor = flavor

    def __eq__(self, other):
        return self.flavor == other.flavor

choco1 = Candy("Choco")
choco2 = Candy("Choco")
milk = Candy("Milk")

print(id(choco1))
print(id(choco2))
print(choco1 == choco2)
def create_deck() -> list[str]:
	"""Return a list of 52 strings containing a standard deck"""
	ranks = ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	suits = ("Hearts", "Diamond", "Clubs", "Spades")

	deck_of_cards = []
	for suit in suits:
		for rank in ranks:
			deck_of_cards.append(f"{rank} of {suit}")
	print(deck_of_cards)
	return deck_of_cards

def draw_top(deck: list[str], count: int=1)-> list[str]:
	"""Remove count return count cards from the start from deck"""

def draw_bottom(deck: list[str], count: int=1) -> list[str]:
	"""Remove and return count cards from the end of the deck"""

def draw_random(deck: list[str], count: int=1) -> list[str]:
	"""Remove and return count random cards from the deck"""

def show(deck):
	"""Print all cards in deck"""

def add_top(deck: list[str], other: list[str]):
	"""Add cards in other to the first parts of deck"""

def add_bottom(deck: list[str], other: list[str]):
	"""Add cards in other to the last parts of deck"""

def add_random(deck: list[str], other: list[str]):
	"""Add cards in other randomly to deck"""

def load(filename: str) -> list[str]:
	"""Returns a list of cards loaded from a file"""

def save(deck: list[str], filename: str):
	"""Saves a list of cards into a file (retrievable with load)"""


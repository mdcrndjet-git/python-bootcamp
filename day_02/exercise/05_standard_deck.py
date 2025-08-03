ranks = ("A","1","2","3","4","5","6","7","8","9","10","J","Q","K")
suits = ("Hearts","Diamond","Clubs", "Spades")

"""
Print every possible pairing of ranks and suits
A of Hearts
2 of Hearts
3 of Hearts
...
K of Hearts
A of Diamonds
2 of Diamonds
3 of Diamonds
"""

for rank in ranks:
    for suit in suits:
        print(f"{rank} of {suit}")
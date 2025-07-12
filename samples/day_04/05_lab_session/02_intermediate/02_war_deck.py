"""
Card Game - War

In this lab session, you will simulate a simple card game called "War" between two players using a deck of 52 cards.
The game will involve drawing cards from the top of the deck, comparing their values, and determining the winner of each round.
The game ends when all cards have been drawn, and the player with the most rounds won is declared the overall winner.

Step 1: Deck Setup
------------------
- The game starts by creating a standard deck of 52 cards.
- The deck is shuffled and divided equally between the two players, giving each player 26 cards.

Step 2: Card Comparison
------------------------
- In each round, both players draw the top card from their deck.
- The value of the card is determined by its rank (e.g., 2 is the lowest, Ace is the highest).
- The player with the higher card wins the round and earns one point.
- If both players draw cards of the same rank, the round is a tie, and no points are awarded.

Step 3: Game Loop
-----------------
- The game continues for 26 rounds (the number of cards in each player’s deck).
- Each round, players compare the cards they draw, update their scores, and proceed to the next round.

Step 4: End of Game
-------------------
- After all 26 rounds have been completed, the game ends.
- The player with the most points is declared the winner.
- If the points are tied, the game ends in a draw.

Optional Enhancements
----------------------
- Implement a "battle" feature where, if both players draw the same card, they each draw 3 additional cards to break the tie.
- Add a feature to display the current scores after each round.
- Allow the game to be saved and loaded from a file, enabling players to resume the game later.
"""

from random import choice


def computer_pick():
    options = ["rock", "scissor", "paper"]

    random_option = choice(options)
    computer_choice = options.index(random_option)

    return computer_choice


def arbiter(player1, player2):
    rules = ("00",  # (0) draw: (player1)rock = (player2)rock
             "01",  # (1) (player1)rock wins: (player1)rock > (player2)scissor
             "02",  # (2) (player2)paper wins: (player1)rock < (player2)paper
             "10",  # (3) (player2)rock wins: (player1)scissor < (player2)rock
             "11",  # (4) draw: (player1)scissor = (player2)scissor
             "12",  # (5) (player1)scissor wins: (player1)scissor > (player2)paper
             "20",  # (6) (player1)paper wins: (player1)paper > (player2)rock
             "21",  # (7) (player2)scissor wins: (player1)paper < (player2)scissor
             "22"  # (8) draw: (player1)paper = (player2)paper
             )
    #print("rules", rules)
    #players_pick = str(f"{player1}{player2}")
    players_pick = player1+player2
    #print("players_pick",players_pick)
    rule_lookup = rules.index(players_pick)

    player1_win = (1, 5, 6)
    player2_win = (2, 3, 7)

    arbiter_result = None
    if rule_lookup in player1_win:
        arbiter_result = 1
    elif rule_lookup in player2_win:
        arbiter_result = 2
    else:
        arbiter_result = 0
    return arbiter_result

print("Choose a weapon:")
print("1 - Rock")
print("2 - Scissor")
print("3 - Paper")
player_1 = int(input("Choose: "))
#print(f"player 1: {player_1}")
player_1 = str(player_1 -1)

player_2 = computer_pick()
#print(f"player 2: {player_2 +1}")
player_2 = str(player_2)

arbiter_decision = arbiter(player_1, player_2)
#print("arbiter_decision: ",arbiter_decision)

if arbiter_decision == 1:
    print("Player 1 wins")
elif arbiter_decision == 2:
    print("Player 2 wins")
else:
    print("It's a draw")
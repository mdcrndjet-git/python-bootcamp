from random import choice

def random_pick():
    # 0 - rock
    # 1 - scissor
    # 2 - paper
    options = ["rock","scissor","paper"]
    random_option = choice(options)
    random_option_index = options.index(random_option)
    return random_option_index

# 0 > 1 = rock > paper
# 0 < 2 = rock < scissor
# 1 < 0 = scissor < rock
# 1 > 2 = scissor > paper
# 2 > 0 = paper > rock
# 2 < 1 = paper < scissor

#options = ["rock", "scissor", "paper"]
computer_pick = random_pick()
#pick = options.index(computer_pick)
print(computer_pick)

computer_pick

#running = True
#while running:
#print("Pick:")
#print("rock")
#print("scissor")
#print("paper")
#choice = input("Choose: ")
#computer_pick = random_pick()
#if choice == computer_pick:
#    print

#if computer_pick == "rock":

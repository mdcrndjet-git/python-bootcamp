ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Change '10','J','Q','K',and 'A' cards to 'Drawn'
ranks[9] = 'Drawn'
ranks[10] = 'Drawn'
ranks[11] = 'Drawn'
ranks[12] = 'Drawn'
ranks[0] = 'Drawn'

# Show the changed list
print(ranks)

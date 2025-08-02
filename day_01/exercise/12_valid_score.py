# Range minimum and maximum bounds
min_number = 0
max_number = 100

# Enter user input
number = int(input("Enter number: "))

# Notify user if the number is a valid score
# Change the variable value here
valid_score = None
valid_score = min_number < number < max_number
print("Valid score: ", valid_score)
# Range minimum and maximum bounds
min_number = 0
max_number = 100

# Enter user input
number = int(input("Enter number: "))

# Notify user if the number is a valid score
# Change the variable value here
valid_score = 0 <= number <= max_number
print("Valid score:", valid_score)

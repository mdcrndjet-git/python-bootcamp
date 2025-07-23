minimum_height = 138

# Ask the user for the following inputs
user_height = float(input("User height (in cm): "))

# Notify user if they can enter the ride
# Change the variable value here
can_enter_ride = user_height >= minimum_height
print("Can enter the ride:", can_enter_ride)

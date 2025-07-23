# Ask the user for an input
user_input = input("Enter number: ")

# Remove extra spaces
user_input = user_input.strip()

if user_input.isnumeric() or user_input[1:].isnumeric():
    user_input = int(user_input)
    print(user_input + 1)
else:
    print("Please enter a valid number!")

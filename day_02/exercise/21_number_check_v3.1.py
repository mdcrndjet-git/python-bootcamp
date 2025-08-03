# Ask the user for an input
user_input = input("Enter number: ")
user_input = user_input.strip()
user_input = user_input.replace(',','')
digits = user_input.split()
user_input = "".join(digits)

# If user enters a valid number
if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input +1)
else:
    # Else
    print("Please enter a valid number!")

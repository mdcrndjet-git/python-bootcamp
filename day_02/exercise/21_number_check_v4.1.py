def clean(string):
    string = string.strip()
    string = string.replace(',','')
    digits = string.split()
    string = "".join(digits)

    return string

# Ask the user for an input
user_input = input("Enter number: ")
user_input = clean(user_input)

# If user enters a valid number
if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input +1)
else:
    # Else
    print("Please enter a valid number!")

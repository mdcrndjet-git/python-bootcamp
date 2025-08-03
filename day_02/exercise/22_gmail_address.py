# Ask the user for an input
email_input = input("Email Address: ")

if email_input.endswith("gmail.com"):
    # If valid gmail address
    print("This is a valid gmail address")
else:
    # Else
    print("This is NOT a valid gmail address")

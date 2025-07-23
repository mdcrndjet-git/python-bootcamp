# Ask the user for their role
role = input("Enter role: ")

# If role is "admin" or role is "editor", print the following
if role == "admin" or role == "editor":
    print("Edit access enabled")
else:
    print("Edit not allowed")

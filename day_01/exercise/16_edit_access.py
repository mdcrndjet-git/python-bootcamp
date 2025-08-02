# Or logical operator

# Ask the user for their role
role = input("Role: ")

# If role is "admin" or role is "editor", print the following
if role == "admin" or role == "editor":
    print("Edit access enabled")
else:
# Else, print: "Access denied"
    print("Edit not allowed")

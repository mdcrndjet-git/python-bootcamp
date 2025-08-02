# If-else condition

# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# If correct_password_given, print: "Access Granted"
# If correct_password_given invalid, print: "Access Denie"
correct_password_given = None

correct_password_given = password_input == correct_password
if correct_password_given:
    print("Access Granted")
else:
    print("Access Denied")

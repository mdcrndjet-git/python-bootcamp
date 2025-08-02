# If condition

# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# Notify user if password is valid
# Change the variable value here
correct_password_given = None

correct_password_given = password_input == correct_password
if correct_password_given:
    print("Access Granted")

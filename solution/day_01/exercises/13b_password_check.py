# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# If correct_password_give, print: "Access Granted"
# If not correct_password, don’t do anything
correct_password_given = correct_password == password_input

if correct_password_given:
    print("Access Granted")

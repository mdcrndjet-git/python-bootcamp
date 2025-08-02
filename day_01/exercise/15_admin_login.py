# And logical operator

# Expected username and password (you can change the value)
correct_username = "admin"
correct_password = "admin"

# Enter username and password
username_input = input("Username: ")
password_input = input("Password: ")

# If username_input equal correct_username
#   and password_input equal correct_password
#   print: "Access Granted"
if username_input == correct_username and password_input == correct_password:
    print("Access Granted")
else:
    # else, print: "Access Denied"
    print("Access Denied")

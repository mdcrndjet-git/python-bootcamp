# Expected username and password(you can change the value)
correct_username = "admin"
correct_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

if username_input == correct_username and password_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

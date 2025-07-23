count = 0
running = True
while running:
    choice = input("Provide command: ")

    if choice == "add":
        count += 1
    elif choice == "sub":
        count -= 1
    elif choice == "double":
        count *= 2
    elif choice == "exit":
        running = False

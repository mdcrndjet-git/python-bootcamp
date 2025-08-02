count = 0
print("Initial count: ", count)

running = True

while running:
    choice = input("Command: ")

    if choice == "add":
        count += 1
    elif choice == "sub":
        count -= 1
    elif choice == "double":
        count *= 2
    elif choice == "exit":
        running = False

    if running:
        print("count: ", count)

print("Output count: ",count)

count = 0
print("Initial count: ", count)

running = True

while running:
    choice = input("Command: ")

    if choice == "add":
        count += 1
        print("count: ", count)
    elif choice == "sub":
        count -= 1
        print("count: ", count)
    elif choice == "double":
        count *= 2
        print("count: ", count)
    elif choice == "exit":
        running = False

print("Output count: ",count)

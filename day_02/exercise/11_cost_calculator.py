def spend(expenses, cost):
    expenses.append(cost)
    return expenses

def refund(expenses):
    expenses.pop(-1)
    return expenses

def show(expenses):
    print(f"All expenses: {expenses}")
    print(f"Total spent: {sum(expenses)}")

def main():
    current_expenses = []
    command = input("command: ")

    while command:
        # Handle command here
        # Example: user inputs "add" -> do add(expenses, cost)
        # Ask the inputs here, not in the function
        if command == "spend":
            try:
                cost_input = float(input("Cost: "))
                if cost_input < 0:
                    raise ValueError()

                current_expenses = spend(current_expenses, cost_input)

            except ValueError:
                print("We don't accept strings or negatives!")

        elif command == "refund":
            current_expenses = refund(current_expenses)

        elif command == "show":
            show(current_expenses)

        # Ask for more
        command = input("Command: ")

main()

def spend(expenses, cost):
    """Add a new cost in the list of expenses"""
    expenses.append(cost)
    print("Spent:\t", cost)


def refund(expenses):
    """Remove the last cost added (if any)"""
    refunded_cost = expenses.pop(-1)
    print("Refunded cost:\t", refunded_cost)


def show(expenses):
    """Print the current list of expenses line-by-line"""
    for index, expense in enumerate(expenses, start=1):
        print(f"Expense #{index}:\t{expense}")

    print("Total expenses:\t", sum(expenses))


def main():
    current_expenses = []
    command = input("Command:\t")

    while command:
        if command == "add":
            new_cost = int(input("New cost:\t"))
            spend(current_expenses, new_cost)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)

        command = input("Command: ")


main()

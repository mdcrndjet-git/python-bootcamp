number = int(input("Pick a number: "))

for sequence in range(11):
    result = number * sequence
    print(f"{number} * {sequence} = {result}")

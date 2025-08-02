# match case condition

# Ask the user input for a color
color_input = input("Please enter a color: ")

# Print the following depending on the color input
match color_input:
    case "green":
        print("Code 1")
    case "yellow":
        print("Code 2")
    case "red":
        print("Code 3")

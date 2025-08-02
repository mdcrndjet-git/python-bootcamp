# if-elseif condition

# Ask the user input for a color
color_input = input("Please enter a color: ")

# Print the following depending on the color input
# if green
#   -> "Go"
# if yellow
#   -> "Wait"
# if red
#   -> "Stop"
if color_input == "green":
    print("Go")
elif color_input == "yellow":
    print("Wait...")
elif color_input == "red":
    print("Stop")
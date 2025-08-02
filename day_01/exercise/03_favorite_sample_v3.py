"""
Create the following variables and fill in the values
Make sire to use the correct data type!
"""
instruction = "Favorite food name: "
favorite_food_name = input(instruction)

instruction = "Cost: "
favorite_food_price = float(input(instruction))
tax = 1.2
cost = favorite_food_price *tax

instruction = "Is the food homemade? "
is_homemade = bool(input(instruction))

# Then, print each information one line at a time
print("Your favorite food name is", favorite_food_name)
print("The cost is ", cost)
print("Is the food homemade? ", is_homemade)

# print variable type used
print(type(favorite_food_name))
print(type(favorite_food_price))
print(type(is_homemade))
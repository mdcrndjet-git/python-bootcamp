string = "I am perfectly calm and everything is fine"

char_counter = {
    "lower case": 0,
    "upper case": 0,
    "space": 0,
}

for char in string:
    if char.isupper():
        char_counter["upper case"] += 1
    elif char.islower():
        char_counter["lower case"] += 1
    elif char.isspace():
        char_counter["space"] += 1

for case, count in char_counter.items():
    print(f"{case} count: {count}")

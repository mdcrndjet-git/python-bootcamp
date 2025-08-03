# Append List: append items in the list

# Initialize empty list of attendees
attendee_names = []

# Ask how many attendees
attendees_count = int(input("Attendee count: "))

# Do this for as many attendees expected
for counter in range(attendees_count):
    attendee_name = input(f"{counter +1} Attendee name: ")

    # Add attendee_name to attendee_names
    attendee_names.append(attendee_name)

# Print attendees
print(attendee_names)

# Initialize empty list of attendees
attendees_names = []
"""
 Append list

"""
# Ask how many attendees
attendees_count = int(input("Attendee count: "))

# Do this for as many attendees expected
for counter in range(attendees_count):
    attendee_name = input(f"{counter +1} Attendee name: ")

    # Add attendee_name to attendee_names
    attendees_names.append(attendee_name)

# Print attendees
print(f"Attendee list: {attendees_names}")

"""
Safely remove from list
"""
# Check and remove attendee name from attendees
remove_attendee_name = "X"
if remove_attendee_name in attendees_names:
    attendees_names.remove(remove_attendee_name)

# Print updated attendees
print(f"Attendee list: {attendees_names}")
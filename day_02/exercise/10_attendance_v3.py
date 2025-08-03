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
 Remove from list using Pop method
"""
#Remove last attendee
remove_attendee_name = attendees_names.pop(-1)

# Print removed last attendee
print(f"Removed attendee name: {remove_attendee_name}")
# Print updated attendees
print(f"Attendee list: {attendees_names}")
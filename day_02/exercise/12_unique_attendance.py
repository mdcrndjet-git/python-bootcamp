attendee_names = set()

attendee_count = int(input("Attendee count: "))

# Do this for as many attendees expected
for counter in range(attendee_count):
    attendee_name = input(f"{counter +1} Attendee name: ")

    # Add attendee_name to attendees_names
    attendee_names.add(attendee_name)

# Remove your name from attendees (if there)
remove_attendee_name = "X"
attendee_names.discard(remove_attendee_name)

print(attendee_names)

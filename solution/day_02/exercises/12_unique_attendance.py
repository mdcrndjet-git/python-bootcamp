attendee_names = set()

attendee_count = int(input("Attendee count: "))

# Do this for as many attendees expected
for attendee in range(attendee_count):
    attendee_name = input("Attendee name: ")

    # Add attendee_name to attendee_names
    attendee_names.add(attendee_name)

print(attendee_names)

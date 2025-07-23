attendee_names = []

attendee_count = int(input("Attendee count: "))

# Do this for as many attendees expected
for attendee in range(attendee_count):
    attendee_name = input("Attendee name: ")

    # Add attendee_name to attendee_names
    attendee_names.append(attendee_name)

print(attendee_names)

# If your name is in attendee_names, remove it
my_name = "Jeff"
if my_name in attendee_names:
    attendee_names.remove("Jeff")

print(attendee_names)

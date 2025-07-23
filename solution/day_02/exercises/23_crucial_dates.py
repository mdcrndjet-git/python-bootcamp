import re

# You can use a custom input
s = "The event is on 12/15/2023, and the deadline is 01/01/2024."

# Print all the dates mentioned
pattern = r'\d{2,4}/\d{2}/\d{2,4}'
print(re.findall(pattern, s))

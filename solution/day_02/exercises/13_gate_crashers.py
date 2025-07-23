invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# Who are all the involved members?
print("Involved Members:", invited | attended)  # union

# Who was absent?
print("Absent:", invited - attended)  # difference

# Who gatecrashed?
print("Not enrolled but attended:", attended - invited)  # difference

# Who was invited and attended
print("Attended properly:", invited & attended)  # intersection

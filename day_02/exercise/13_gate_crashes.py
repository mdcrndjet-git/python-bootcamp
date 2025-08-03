invited = {"Ana","Ben","Carlo","Dani"}
attended = {"Ben", "Carlo","Ely"}
"""
Set UNION
"""
# Who are all the involved
involved = invited.union(attended)  # Alt: invited |attended
print("Involved Members:", involved)
"""
Set DIFFERENCE (left result)
"""
# Who was absent
absent = invited.difference(attended)   # Alt: invited -attended
print("Absent:", absent)
"""
Set DIFFERENCE (right result)
"""
# Who gatecrashed?
gatecrashed = attended.difference(invited)  # Alt: attended -invited
print("Not enrolled but attended:", gatecrashed)
"""
Set INTERSECTION
"""
# Who was invited and attended
attended_properly = invited.intersection(attended)  # Alt:
print("Attended properly:", attended_properly)
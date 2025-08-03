mission = "Orbiter Alpha"
distance_km = 1500000.4567
duration_days = 92.5
speed = distance_km / (duration_days * 24)

print("Mission Log ")
print(f"Mission: {mission}")
print(f"Distance: {distance_km} km")
print(f"Duration: {duration_days} days")
print(f"Speed: {speed} km/h")

#  Mission Log
# Mission: Orbiter Alpha
# Distance: 1,500,000.46 km
# Duration: 92.50 days
# Speed: 675.68 km/h
print("Mission Log ")
print(f"Mission: {mission}")
print(f"Distance: {distance_km:,.2f} km")
print(f"Duration: {duration_days} days")
print(f"Speed: {speed:,.2f} km/h")

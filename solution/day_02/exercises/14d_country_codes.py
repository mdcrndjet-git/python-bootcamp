# Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "SG": "Singapore",
}

# Print the country for the given country code
# If the key is not found, print Unknown
country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))

# Print all codes
print("Codes:", country_codes.keys())

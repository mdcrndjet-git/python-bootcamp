# Add country codes
country_codes = {
    "PH":"Philippines",
    "US":"United States of America",
    "RU":"Russia",
    "AU":"Australia",
    "IN":"India",
    "UK":"United Kingdom",
    "CA":"Canada",
    "SP":"Spain",
    "SG":"Singapore",
}

print(country_codes)

print(country_codes["PH"])

country_code = input("Country code: ")
print(country_codes.get(country_code))

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

print("Countries:")
for key, value in country_codes.items():
    print(key, value)

print(country_codes["PH"])

if "JP" in country_codes:
    print("Japan already exists")
else:
    country_codes["JP"] = "Japan"

country_code = input("Country code: ")
print(country_codes.get(country_code, "Unknown"))

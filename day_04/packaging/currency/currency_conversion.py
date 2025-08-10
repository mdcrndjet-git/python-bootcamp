import requests

# Send request
site = "https://open.er-api.com/v6/latest/USD"
response = requests.get(site)

# Get latest conversion rate form USD to PHP
if response.status_code == 200:
    print("Success")
    #print(response.text)
    rates = response.json()
    print(rates)
    currency = rates['rates']
    print("USD-to-PHP = ",currency["PHP"])

else:
    print("Error occurred: ",response.status_code)


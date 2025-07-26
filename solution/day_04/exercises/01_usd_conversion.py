import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP
try:
    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        usd_to_php = rates['PHP']
        print("Conversion rate (USD to PHP):", usd_to_php)
    else:
        print(response.text)
except Exception as e:
    print("Failed to get data from API with error:", e)

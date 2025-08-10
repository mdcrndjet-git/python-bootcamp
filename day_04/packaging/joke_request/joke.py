import requests

# Send request
site = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(site)

if response.status_code == 200:
    print("Success")

    joke = response.json()
    print(joke['setup'])
    print(joke['punchline'])
else:
    print("Error occurred: ",response.status_code)

import requests

API_KEY = "605118a2-f287-4659-b058-8b9cbc7c686b"
DOMAIN = "github.com"

url = f"https://api.builtwith.com/v20/api.json?KEY={API_KEY}&LOOKUP={DOMAIN}"

response = requests.get(url)
if response.status_code == 200:
    print(response.json())  # Prints analytics tools used
else:
    print(f"Error: {response.status_code}, {response.text}")

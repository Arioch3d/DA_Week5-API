import pandas as pd
import requests
'''
Works But Empty DataFrame for some reason
dnd_url = "https://api.open5e.com"
response = requests.get(dnd_url)

if response.status_code == 200:
    data = response.json()
    print('success!')

else:
    print(f"Error: {response.status_code}")

df = pd.DataFrame()
print(df)
'''

dnd_url = "https://www.dnd5eapi.co/api/2014"
response = requests.get(dnd_url)

payload = {}
headers = {
    'Accept':'application/json'
}
if response.status_code == 200:
    response = requests.request("GET", dnd_url, headers=headers, data=payload)
    data = response.json()
    print('success!')

else:
    print(f"Error: {response.status_code}")
print(response.text)
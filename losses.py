import json
import requests
url = 'https://manifold.markets/api/v0/users?limit=1000'
response = requests.get(url).json()
output = []
while response:
  for user in response:
    if user['profitCached']['allTime'] < -15000:
      output.append(user)
  response = requests.get(url + '&before=' + response[-1]['id']).json()
print(json.dumps(output, indent=1))

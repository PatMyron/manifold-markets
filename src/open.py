import json
import requests
url = 'https://manifold.markets/api/v0/markets?limit=1000'
response = requests.get(url).json()
output = []
while response:
  for market in response:
    if not market['isResolved']:
      output.append(market)
  response = requests.get(url + '&before=' + response[-1]['id']).json()
print(json.dumps(output, indent=1))

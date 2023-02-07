import requests
url = 'https://manifold.markets/api/v0/markets?limit=1000'
response = requests.get(url).json()
output = []
while response:
  output.extend(response)
  response = requests.get(url + '&before=' + response[-1]['id']).json()
print(output)

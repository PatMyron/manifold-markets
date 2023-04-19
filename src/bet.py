import json
import os
import requests
url = 'https://manifold.markets/api/v0/bet'
body = {
    "contractId": "NEpTIkMlf9EZY9PBTyB3",
    "amount": 1,
    "outcome": "YES",
    "limitProb": 0.01
}
headers = {
    "Authorization": f"Key {os.getenv('API_KEY')}"
}
print(requests.post(url, json=body, headers=headers).json())

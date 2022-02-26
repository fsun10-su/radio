import requests
import json
import os

def random(num):
    url = 'https://api.random.org/json-rpc/2/invoke'

    data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "1bf71ed9-6f41-4f73-b96a-606fd7835a79",
            "n": 1,
            "min": 0,
            "max": num,
            'replacement': False
        },
        "id": 42
    }

    response = requests.post(url, json=data)
    all = response.json()
    result = all['result']['random']['data'][0]
    return result



random(10)
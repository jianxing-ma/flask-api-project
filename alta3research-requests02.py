#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/inventory"

new_motorcycle = {
    "brand": "BMW",
    "model": "S1000RR",
    "year": 2023,
    "engine_capacity": 999,
    "color": "White",
    "price": 18500.00,
    "features": ["Dynamic Traction Control", "Launch Control", "Full LED lighting"],
}


# json.dumps takes a python object and returns it as a JSON string
new_motorcycle = json.dumps(new_motorcycle)

# requests.post requires two arguments at the minimum;
# a url to send the request
# and a json string to attach to the request
resp = requests.post(URL, json=new_motorcycle)

# pretty-print the response back from our POST request
pprint(resp.json())

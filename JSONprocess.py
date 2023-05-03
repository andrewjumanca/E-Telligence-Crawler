import json
import os

# This file is responsible for the functions used within spiders for writing to JSON
# Will also probably use this in the dom_filteration.py to send links to NetPrism api.
def append_to_json(data):
    filename = 'product_data.json'
    
    # Check if file exists and is not empty
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            json_data = json.load(f)
            json_data['products'].append(data)
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)
    else:
        # Initialize structure and store elements
        json_data = {'products': [data]}
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)

def readFromJSON():
    with open('product_data.json', 'r') as f:
        URLs = json.load(f)
    return URLs
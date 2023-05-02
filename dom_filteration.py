# Code to connect to Netprism API

import base64
import os
import requests
from dotenv import load_dotenv


# CODE TO SET UP NETPRISM ENDPOINT
print('starting netprism connection')
netprism_api_url = 'https://canary.netprism.dev/v1/task'
load_dotenv()
api_key = os.getenv('API_KEY')
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
request_body = {
    'url': 'https://www.walmart.com/ip/Scoop-Women-s-Long-Sleeve-Fit-and-Flare-Poplin-Short-Shirt-Dress/1845870476?athbdg=L1103&from=browseResults',
    'type': 'webpage',
    'options': {
        'jsRender': True
    }
}

response2 = requests.post(netprism_api_url, headers=headers, json=request_body)
response_json = response2.json()
print(response2.json())
# Retrieve the task ID from the response
data = response_json['data']
print(data)
decoded_html = base64.b64decode(data)
print(decoded_html)
print('finished netprism connection')
with open("output.txt", "w") as f:
    # Write some text to the file
    f.write(decoded_html.decode('utf-8'))
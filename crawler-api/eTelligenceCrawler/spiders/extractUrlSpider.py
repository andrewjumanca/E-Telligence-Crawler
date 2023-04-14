import scrapy
import requests
from urllib.parse import urlparse, parse_qsl
from dotenv import load_dotenv
import os
import base64

class extractUrlSpider(scrapy.Spider):
    name = "extractUrlSpider"

    def __init__(self, product_name = "", urls=[],  **kwargs):
        super().__init__(**kwargs)
        self.urls = urls
        self.product_name = product_name
        self.product_data = {'product_name': self.product_name,
                    'urls': []}

    def start_requests(self):
        for url in self.urls:

            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        actual_url = extract_actual_url(response.url)
        if actual_url not in self.product_data['urls']:
            self.product_data['urls'].append(actual_url)

    def closed(self, reason):
        try:
            response = requests.post('http://localhost:8000/api/v1/send', json=self.product_data)
            if response.status_code == 200:
                    print('Data sent successfully')
        except Exception as e:
            print(e)    

def extract_actual_url(google_url):
    parsed_url = urlparse(google_url)
    query_params = dict(parse_qsl(parsed_url.query))
    actual_url = query_params.get('url', '')
    return actual_url


# Code to connect to Netprism API

# print('starting netprism connection')
# netprism_api_url = 'https://canary.netprism.dev/v1/task'
# load_dotenv()
# api_key = os.getenv('API_KEY')
# headers = {
#     'Authorization': f'Bearer {api_key}',
#     'Content-Type': 'application/json'
# }
# request_body = {
#     'url': 'https://www.champion.com/closed-bottom-jersey-pants.html?country=US&currency=USD',
#     'type': 'webpage',
#     'options': {
#         'jsRender': True
#     }
# }
# response2 = await requests.post(netprism_api_url, headers=headers, json=request_body)
# response_json = response2.json()
# print(response2.json)
# # Retrieve the task ID from the response
# data = response_json['data']
# decoded_html = base64.b64decode(data)
# print(decoded_html)
# print('finished netprism connection')
# with open("output.txt", "w") as f:
#     # Write some text to the file
    # f.write(decoded_html.decode('utf-8'))
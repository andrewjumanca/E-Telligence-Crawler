import scrapy
import requests
import os
from urllib.parse import urlparse, parse_qsl
from dotenv import load_dotenv


class extractUrlSpider(scrapy.Spider):
    name = "extractUrlSpider"

    def __init__(self, product_name = "", urls=[],  **kwargs):
        super().__init__(**kwargs)
        self.urls = urls
        self.product_name = product_name
        self.product_data = {'product_name': self.product_name,
                    'urls': []}

    def start_requests(self):
        print('url length', len(url))
        for url in self.urls:

            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        actual_url = extract_actual_url(response.url)

        if actual_url not in self.product_data['urls']:

            self.product_data['urls'].append(actual_url)

    def closed(self, reason):
        # Save self.product_data to a database or file
        try:
            netprism_api_url = 'https://canary.netprism.dev/v1/task'


            load_dotenv()
            api_key = os.getenv('API_KEY')
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            request_body = {
                'url': actual_url,
                'type': 'webpage',
                'options': {
                    
                }
            }
            # response = requests.post(self.netprism_api_url, headers=self.headers, json=request_body)
            # response_json = response.json()
            # print(response.json)
            # # Retrieve the task ID from the response
            # task_id = response_json['id']

            response = requests.post('http://localhost:3000/api/v1/send', json=self.product_data)
            if response.status_code == 200:
                    print(self.product_data['urls'])
        except Exception as e:
            print(e)

def extract_actual_url(google_url):
    parsed_url = urlparse(google_url)
    query_params = dict(parse_qsl(parsed_url.query))
    actual_url = query_params.get('url', '')
    return actual_url

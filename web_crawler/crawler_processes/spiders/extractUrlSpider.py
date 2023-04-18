import scrapy
import requests
from urllib.parse import urlparse, parse_qsl

class extractUrlSpider(scrapy.Spider):
    name = "extractUrlSpider"

    def __init__(self, response=None, callback=None, product_name = "", urls=[], *args, **kwargs):
        super().__init__(**kwargs)
        self.urls = urls
        self.product_name = product_name
        self.product_data = {'product_name': self.product_name,'urls': []}
        self.response = response
        self.callback = callback

    def start_requests(self):
        # Get response from parent spider (Google, Bing, etc.)
        output = []        
        for url in self.urls:
            output.append(scrapy.Request(url=url, callback=self.parse))
        self.callback(output)

    def parse(self, response):
        actual_url = extract_actual_url(response.url)
        if actual_url not in self.product_data['urls']:
            self.product_data['urls'].append(actual_url)

    # def closed(self, reason):
    #     try:
    #         response = requests.post('http://localhost:3000/api/v1/send', json=self.product_data)
    #         if response.status_code == 200:
    #                 print('Data sent successfully')
    #     except Exception as e:
    #         print(e)

def extract_actual_url(google_url):
    parsed_url = urlparse(google_url)
    query_params = dict(parse_qsl(parsed_url.query))
    actual_url = query_params.get('url', '')
    return actual_url

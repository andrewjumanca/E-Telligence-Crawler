import scrapy
import requests
import json
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"

    def __init__(self, search_query='', **kwargs):
        super().__init__(**kwargs)
        self.search_query = search_query

    def start_requests(self):
        url = f'https://www.google.com/search?q={self.search_query}&source=lnms&tbm=shop'
        yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        product_data = {'product_name': self.search_query,
                    'urls': []}

        queryRegex = convert_string_to_regex(self.search_query)
        print(queryRegex)
        
        link_extractor = LinkExtractor(allow=(rf'{queryRegex}',))

        # r'.*Jordan\+Essential\+Winter\+Mens\+Fleece\+Hoodie.*'

        for link in link_extractor.extract_links(response):
            product_data['urls'].append(link.url)
       
        try:
            response = requests.post('http://localhost:3000/api/v1/send', json=product_data)
            if response.status_code == 200:
                    print('Data sent successfully')
        except Exception as e:
            print(e)
    

def convert_string_to_regex(string):
    # Remove leading/trailing white space and replace internal white space with '+'
    string = re.sub(r'\s+', '+', string.strip())
    # Add escape slashes to each space in the modified string
    string = re.sub(r'\+', r'\+', string)
    # Wrap the modified string in the regex syntax
    return rf'.*{string}.*'
    

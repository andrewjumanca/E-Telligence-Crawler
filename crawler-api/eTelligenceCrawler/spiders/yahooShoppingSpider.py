import scrapy
import requests
import json
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
# from spiders.extractUrlSpider import extractUrlSpider

class yahooShoppingSpider(scrapy.Spider):
    name = "yahooShoppingSpider"

    def __init__(self, search_query='', **kwargs):
        super().__init__(**kwargs)
        self.search_query = search_query
        self.product_data = {'product_name': "Yahoo:" + self.search_query,
                    'urls': []}

    def start_requests(self):
        url = f'https://shopping.yahoo.com/search?p={self.search_query}&renderBySimilarity=1'
        yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        
        link_extractor = LinkExtractor(restrict_xpaths='//a[contains(@href, "product")]')
    
        for link in link_extractor.extract_links(response):

            self.product_data['urls'].append(link.url)

        print(self.product_data['urls'])
        
        with open('product_data.json', 'a+') as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write('\n')

            f.write(json.dumps(self.product_data, indent=4))

        # for link in self.product_data['urls']:
        #     yield scrapy.Request(url=link, callback=self.parse_found_URLS)

        # try:
        #     response = requests.post('http://localhost:3000/api/v1/send', json=self.product_data)
        #     if response.status_code == 200:
        #             print('Data sent successfully')
        # except Exception as e:
        #     print(e)    
    
    def parse_found_URLS(self, response):
        print(response)



def check_word_repetition(url_string, word):
    url_string = url_string.lower()
    word_count = url_string.count(word.lower())
    return word_count > 1



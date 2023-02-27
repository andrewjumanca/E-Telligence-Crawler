import scrapy
import requests
import json
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"

    def __init__(self, search_query='', **kwargs):
        super().__init__(**kwargs)
        self.search_query = search_query

    # def __init__(self, search_term='', **kwargs):
    #     super().__init__(**kwargs)
    #     self.search_query = search_term

    def start_requests(self):
        url = f'https://www.google.com/search?q={self.search_query}&source=lnms&tbm=shop'
        # url = f'https://www.google.com/search?q={self.search_query}'
        # url = f'https://etelligenceapi.live/search?q={self.search_query}'
        yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        product_data = {'product_name': self.search_query,
                    'urls': []}
        
        link_extractor = LinkExtractor(allow=(r'url\?url=https',), )
        # allow=(rf'{queryRegex}',)
        # allow=(r'url\?url=https',)
    
        for link in link_extractor.extract_links(response):

            if not check_word_repetition(link.url, "google.com"):
                product_data['urls'].append(link.url)
            # product_data['urls'].append(link.url)
        try:
            print("Array length: ", len(product_data['urls']))
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

def check_word_repetition(url_string, word):
    # Convert the URL string to lowercase to make the search case-insensitive
    url_string = url_string.lower()
    
    # Count the occurrences of the word in the URL string
    word_count = url_string.count(word.lower())
    
    # Return True if the word appears more than once in the URL string, False otherwise
    return word_count > 1



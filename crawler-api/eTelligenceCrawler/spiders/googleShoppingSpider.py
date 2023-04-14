import scrapy
import requests
import json
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
from spiders.extractUrlSpider import extractUrlSpider

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
        
        link_extractor = LinkExtractor(allow=(r'url\?url=https',), )
    
        for link in link_extractor.extract_links(response):

            if not check_word_repetition(link.url, "google.com"):
                product_data['urls'].append(link.url)

        process = CrawlerProcess(get_project_settings())
        process.crawl(extractUrlSpider, product_name = product_data['product_name'], urls = product_data['urls'])
        process.start()


def check_word_repetition(url_string, word):
    url_string = url_string.lower()
    word_count = url_string.count(word.lower())
    return word_count > 1



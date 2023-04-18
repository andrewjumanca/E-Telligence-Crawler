from pathlib import Path
import scrapy
from scrapy.linkextractors import LinkExtractor
import json


def check_word_repetition(url_string, word):
    url_string = url_string.lower()
    word_count = url_string.count(word.lower())
    return word_count > 1

class LinksSpider(scrapy.Spider):
    name = "links"
    links = []

    def __init__(self, searchQuery="", *args, **kwargs):
        super(LinksSpider, self).__init__(*args, **kwargs)
        self.searchQuery = searchQuery

    def start_requests(self):
        print("SEARCH QUERY IN SPIDER: ", self.searchQuery)
        yield scrapy.Request(url=f'https://www.google.com/search?q={self.searchQuery}&source=lnms&tbm=shop', callback=self.parse)

    def parse(self, response):
        # Extract all HTTP URLs from the response
        link_extractor = LinkExtractor()
        for link in link_extractor.extract_links(response):
            if not check_word_repetition(link.url, "google.com"):
                self.links.append(link.url)

        
    # def parse_http_urls(self, response):
    #     # Extract all HTTP URLs from the response
    #     http_urls = response.css('a[href^="http"]::attr(href)').getall()

    #     # Add the HTTP URLs to the all_urls list
    #     self.links.extend(http_urls)


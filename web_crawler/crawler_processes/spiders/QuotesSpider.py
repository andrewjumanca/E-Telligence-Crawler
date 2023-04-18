from pathlib import Path
import scrapy
from scrapy.linkextractors import LinkExtractor
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        links = [link for link in links if link.startswith('http')]
        result = {'': [], 'links': links}
        return result
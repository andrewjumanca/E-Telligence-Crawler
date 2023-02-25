import scrapy
from scrapy.linkextractors import LinkExtractor
#from fake_useragent import UserAgent


class searxngCrawler(scrapy.Spider):
    name = "searxngCrawler"
    # ua = UserAgent()        #The crawler works without lines 8 and 9 but idk leaving it for now just in case
    # USER_AGENT = ua.random
    start_urls = [
        #This is the url for search engine. Have to manually type in the search terms for this one.
        'https://etelligenceapi.live/search?q='
    ]

    def parse(self, response):
        for product in response.css("article.result"):
            yield {
                'Link Title': product.css("a::text").extract_first(),
                'URL': product.css("a.url_wrapper::attr(href)").extract_first(),
            }

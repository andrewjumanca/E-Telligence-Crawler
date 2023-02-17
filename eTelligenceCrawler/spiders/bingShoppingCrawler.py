import scrapy
from scrapy.linkextractors import LinkExtractor
from fake_useragent import UserAgent


class bingShopingCrawler(scrapy.Spider):
    name = "bingShoppingCrawler"
    ua = UserAgent()         #The crawler works without lines 8 and 9 but idk leaving it for now just in case
    USER_AGENT = ua.random
    start_urls = [
        # This is just a random url from bing shopping for now
    ]

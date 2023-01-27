import scrapy
from scrapy.linkextractors import LinkExtractor
from fake_useragent import UserAgent


class googleShopingCrawler(scrapy.Spider):
    name = "googleShoppingCrawler"
    ua = UserAgent()         #The crawler works without lines 8 and 9 but idk leaving it for now just in case
    USER_AGENT = ua.random
    start_urls = [
        # This is just a random url from google shopping for now
        'https://www.google.com/search?q=Jordan+Essential+Winter+mens+fleece+hoodie&sxsrf=AJOqlzVcDDvf7V-9QSLWJxt7BoB_o0iXag:1674173548345&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjbw5C97tT8AhVxJ30KHSUaBewQ_AUoAXoECAEQAw&biw=1269&bih=725&dpr=2'
    ]

    def parse(self, response):
        for product in response.css("div.KZmu8e"):
            yield {
                'product': product.css("h3.sh-np__product-title::text").extract_first(),
                'brand': product.css("span.E5ocAb::text").extract_first(),
            }

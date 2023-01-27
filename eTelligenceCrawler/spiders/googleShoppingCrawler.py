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
        for product in response.css("div.sh-dgr__gr-auto.sh-dgr__grid-result"):
            yield {
                'product_name': product.css("h3.tAxDx::text").extract_first(),
                'brand': product.css("div.aULzUe.IuHnof::text").extract_first(),
                'price': product.css("span.a8Pemb.OFFNJ::text").extract_first(),
                'URL': product.css("a.Lq5OHe.eaGTj.translate-content::attr(href)").extract_first()
            }

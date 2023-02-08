import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"
    start_urls = []

    def parse(self, response):
        for product in response.css("div.sh-dgr__content"):
            #pageNum = response.css('td.YyVfkd span::text').extract_first()
            yield {
                #'page': pageNum,
                'product_name': product.css("h4.tAxDx::text").extract_first(),
                'brand': product.css("div.aULzUe.IuHnof::text").extract_first(),
                'price': product.css("span.a8Pemb.OFFNJ::text").extract_first(),
                'URL': product.css("a.Lq5OHe.eaGTj.translate-content::attr(href)").extract_first()
            }
        
import scrapy
import requests
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"
    start_urls = ["https://www.google.com/search?q=Jordan+Essential+Winter+mens+fleece+hoodie&sxsrf=AJOqlzVcDDvf7V-9QSLWJxt7BoB_o0iXag:1674173548345&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjbw5C97tT8AhVxJ30KHSUaBewQ_AUoAXoECAEQAw&biw=1269&bih=725&dpr=2"]

    product_data = {'product_name': "placeholder",
                    'urls': []}
    def parse(self, response):
        product_data = []
        for product in response.css("div.sh-dgr__content"):
            #pageNum = response.css('td.YyVfkd span::text').extract_first()
            url = {
                #'page': pageNum,
                # 'product_name': product.css("h4.tAxDx::text").extract_first(),
                # 'brand': product.css("div.aULzUe.IuHnof::text").extract_first(),
                # 'price': product.css("span.a8Pemb.OFFNJ::text").extract_first(),
                'URL': product.css("a.Lq5OHe.eaGTj.translate-content::attr(href)").extract_first()
            }
            product_data['urls'].append(url['URL'])
            # Make a POST request to the API endpoint
        try:
            response = requests.post('http://localhost:3000/api/v1/send', json=product_data)
            if response.status_code == 200:
                    print('Data sent successfully')
        except Exception as e:
            print(e)

        
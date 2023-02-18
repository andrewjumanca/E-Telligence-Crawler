import scrapy
import requests
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"
    start_urls = ["https://www.google.com/search?q=Jordan+Essential+Winter+mens+fleece+hoodie&sxsrf=AJOqlzVcDDvf7V-9QSLWJxt7BoB_o0iXag:1674173548345&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjbw5C97tT8AhVxJ30KHSUaBewQ_AUoAXoECAEQAw&biw=1269&bih=725&dpr=2"]

    def parse(self, response):
        product_data = {'product_name': "placeholder",
                    'urls': []}
        
        link_extractor = LinkExtractor()

        for link in link_extractor.extract_links(response):
            product_data['urls'].append(link.url)
       
        try:
            response = requests.post('http://localhost:3000/api/v1/send', json=product_data)
            if response.status_code == 200:
                    print('Data sent successfully')
        except Exception as e:
            print(e)

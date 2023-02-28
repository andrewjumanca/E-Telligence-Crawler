import sys
import scrapy as scrapy
from spiders.googleShoppingSpider import googleShoppingSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings




if __name__ == "__main__":

  search_term = sys.argv[1]
  
  process = CrawlerProcess(get_project_settings())
  

  process.crawl(googleShoppingSpider,  search_query = search_term)

  process.start()

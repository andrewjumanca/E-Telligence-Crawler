from googleShoppingSpider import googleShoppingSpider
from bingShoppingSpider import bingShoppingSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


if __name__ == "__main__":
  process = CrawlerProcess(get_project_settings())
  urls = {
    'google': ['https://www.google.com/search?q={SEARCH_PARAM}&sxsrf=AJOqlzVcDDvf7V-9QSLWJxt7BoB_o0iXag:1674173548345&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjbw5C97tT8AhVxJ30KHSUaBewQ_AUoAXoECAEQAw&biw=1269&bih=725&dpr=2'],
    'bing': ['https://www.bing.com/shop?q={SEARCH_PARAM}&FORM=SHOPTB'],
    'walmart': ['https://www.walmart.com/search?q={SEARCH_PARAM}'],
    'bestbuy': ['https://www.bestbuy.com/site/searchpage.jsp?st={SEARCH_PARAM}&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'],
    'amazon': ['https://www.amazon.com/s?k={SEARCH_PARAM}&crid=24UV5RNNGK2MJ&sprefix={SEARCH_PARAM}%2Caps%2C152&ref=nb_sb_noss_1']
  }

  def setSearchParams(self, searchTerm):
    searchTerm = searchTerm.replace(" ", "+")
    for name in urls.keys():
      urls[name][0] = urls[name][0].replace("{SEARCH_PARAM}", searchTerm)

  process.crawl(googleShoppingSpider, custom_settings={
    'FEED_URI': 'googleShoppingResults.json',
    'FEED_FORMAT': 'json',
    'START_URLS': urls['google']
    
    })
  
  process.crawl(bingShoppingSpider, custom_settings={
    'FEED_URI': 'bingResults.json',
    'FEED_FORMAT': 'json',
    'START_URLS': urls['bing']
    
    })
  process.start()
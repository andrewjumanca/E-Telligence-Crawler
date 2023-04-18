import scrapy
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from web_crawler.crawler_processes.spiders.LinksSpider import LinksSpider

# Configure Logging & Import Project Settings
settings = get_project_settings()

# Establish MongoDB Pipeline
mongo_uri = settings.get('MONGO_URI')
mongo_db = settings.get('MONGO_DATABASE')
mongo_collection = settings.get('MONGO_COLLECTION')

# MongoDB Model Structure
class Product:
    def __init__(self, searchQuery, URLs):
        self.searchQuery = searchQuery
        self.URLs = URLs
    
    def to_dict(self):
        return {'searchQuery': self.searchQuery, 'URLs': self.URLs}

# Start FastAPI app
app = FastAPI()

@app.get("/")
async def scrape_endpoint(searchQuery: str = Query(..., description="Product search term")):
    configure_logging()
    runner = CrawlerRunner(settings)

    spider = LinksSpider

    d = runner.crawl(spider, searchQuery=searchQuery)

    # Add a callback to the deferred object to store the list of URLs in a variable
    d.addCallback(lambda _: setattr(spider, "result", spider.links))
    d.addBoth(lambda _: reactor.stop())

    # Start the Twisted reactor
    reactor.run()
    urls = LinksSpider.result

    client = MongoClient('mongodb+srv://admin:pa33word@crawler.0jer4eh.mongodb.net/test')
    db = client['crawler']
    data = db.scrapeResults

    results = Product(searchQuery, urls)
    data.insert_one(results.to_dict())

    return JSONResponse(content=results.to_dict())
    # return {"message": "Scraping for {searchQuery} completed"}


# ------------------------------------------------------------------------------------------------------------ #

# configure_logging()
# runner = CrawlerRunner(settings)

# spider = LinksSpider

# def stop_reactor():
#     try:
#         reactor.stop()
#     except ReactorNotRunning:
#         pass

# d = runner.crawl(spider)
# # runner.crawl(spider2)
# # d.runner.join() (for multiple spiders)

# # Add a callback to the deferred object to store the list of URLs in a variable
# d.addCallback(lambda _: setattr(spider, "result", spider.links))
# d.addBoth(lambda _: reactor.stop())

# # Start the Twisted reactor
# reactor.run()

# # Store the list of URLs in a variable
# urls = LinksSpider.result
# print("**********************************************************")
# print("**********************************************************")
# print(urls)

# ------------------------------------------------------------------------------------------------------------ #
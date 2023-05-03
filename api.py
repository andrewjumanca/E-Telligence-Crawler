import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from web_crawler.crawler_processes.spiders.googleShoppingSpider import googleShoppingSpider
from pymongo import MongoClient
from JSONprocess import readFromJSON
import json

# Wrapper class for URL data before sending to MongoDB (offline right now)
class Product:
    def __init__(self, searchQuery, URLs):
        self.searchQuery = searchQuery
        self.URLs = URLs
    
    def to_dict(self):
        return {'searchQuery': self.searchQuery, 'URLs': self.URLs}

# Wrapper class to instantiate CrawlerProcess for each spider
class SpiderRunner(Process):
    def __init__(self, spider, queue, searchQuery):
        Process.__init__(self)
        self.queue = queue
        self.searchQuery = searchQuery
        self.spider = spider

    def run(self):
        process = CrawlerProcess(get_project_settings())
        # spider_cls = process.spider_loader.load(self.spider_name)
        # spider = spider_cls(searchQuery=self.searchQuery)
        process.crawl(self.spider, searchQuery=self.searchQuery)
        process.start()
        process.stop()
        self.queue.put('done')

app = FastAPI()

@app.get("/scrape/")
async def scrape(searchQuery: str = Query(..., description="Product search term")):
    with open('product_data.json', 'w') as f:
        f.truncate(0)
    spiders = [googleShoppingSpider]
    queue = Queue()

    for spider in spiders:
        spider_runner = SpiderRunner(spider, queue, searchQuery=searchQuery)
        spider_runner.start()

    for spider in spiders:
        queue.get()

    # with open('product_data.json', 'r') as f:
    #     URLs = json.load(f)

    # client = MongoClient('mongodb+srv://admin:pa33word@crawler.0jer4eh.mongodb.net/test')
    # db = client['crawler']
    # data = db.scrapeResults

    # results = Product(searchQuery, URLs)
    # data.insert_one(results.to_dict())
    return JSONResponse(content=readFromJSON())
    # return {"message": "Scraping completed!"}

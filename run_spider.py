import sys

# Set Twisted reactor BEFORE importing anything Scrapy-related
sys.setrecursionlimit(10000)  # Optional, just in case
import asyncio
import scrapy

from twisted.internet import asyncioreactor
try:
    asyncioreactor.install()
except Exception:
    pass  # Avoids double-install errors

# Now import the rest
from scrapy.crawler import CrawlerProcess
from spider_laser_amazon.spiders.engraver import EngraverSpider

process = CrawlerProcess()
process.crawl(EngraverSpider)
process.start()

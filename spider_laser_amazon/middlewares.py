# spider_laser_amazon/middlewares.py

import random
from scrapy import signals

class ScraperAPIMiddleware:
    def process_request(self, request, spider):
        api_key = spider.settings.get('SCRAPERAPI_KEY')
        if api_key:
            original_url = request.url
            scraperapi_url = f'http://api.scraperapi.com/?api_key={api_key}&url={original_url}'
            request._set_url(scraperapi_url)
        return None

class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agents=crawler.settings.get('USER_AGENT_LIST'))

    def process_request(self, request, spider):
        if self.user_agents:
            request.headers['User-Agent'] = random.choice(self.user_agents)

import scrapy
from scrapy_selenium import SeleniumRequest


class EngraverSpider(scrapy.Spider):
    name = "engraver"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=laser+engraver"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5
            )

    def parse(self, response):
        products = response.xpath('//div[@data-component-type="s-search-result"]')

        for product in products:
            title = product.xpath('.//h2//span/text()').get()

            # Try multiple ways to extract the product URL
            url = product.xpath('.//a[@class="a-link-normal s-no-outline"]/@href').get()
            if not url:
                url = product.xpath('.//a[contains(@href, "/dp/")]/@href').get()
            full_url = response.urljoin(url) if url else None

            # Price
            price_whole = product.xpath('.//span[@class="a-price-whole"]/text()').get()
            price_fraction = product.xpath('.//span[@class="a-price-fraction"]/text()').get()
            price = f"${price_whole}.{price_fraction}" if price_whole and price_fraction else None

            # Rating
            rating = product.xpath('.//span[@class="a-icon-alt"]/text()').get()

            yield {
                'title': title.strip() if title else None,
                'price': price,
                'url': full_url,
                'rating': rating.strip() if rating else None,
            }

        # Handle pagination - go to the next page if it exists
        next_page = response.xpath('//a[contains(@class, "s-pagination-next")]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield SeleniumRequest(
                url=next_page_url,
                callback=self.parse,
                wait_time=5
            )

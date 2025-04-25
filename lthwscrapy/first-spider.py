import scrapy
from scrapy.crawler import CrawlerProcess

class FirstSpider(scrapy.Spider):
    name = "first_spider"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# initialize the CrawlerProcess
process = CrawlerProcess()

# start the crawling process
process.crawl(FirstSpider)

# run the crawler
process.start()

# stop the crawler
process.stop()
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.example.com/blog']

    def parse(self, response):
        for title in response.css('.post-title'):
            yield {
                'title': title.css('::text').get()
            }
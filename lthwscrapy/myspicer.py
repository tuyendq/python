import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    def start_requests(self):
        # Define the URL to scrape
        urls = ['https://example.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract the title of the page
        title = response.css('title::text').get()

        # Extract all paragraphs
        paragraphs = response.css('p::text').getall()

        # Extract links
        links = response.css('a::attr(href)').getall()

        # Print extracted data
        self.log(f'Title: {title}')
        self.log(f'Paragraphs: {paragraphs}')
        self.log(f'Links: {links}')
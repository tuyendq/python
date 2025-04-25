import scrapy
from scrapy.crawler import CrawlerProcess
class DataCampSpider(scrapy.Spider):
    name = 'datacamp spider'

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses-all']     
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.status)  # Print the response text for debugging
        # courses = response.css('section.css-10jrqpr').getall()
        # for course in courses:
        #     yield {
        #         'title': course.css('h2::text').get(),
        #         'link': course.css('a::attr(href)').get(),
        #         'description': course.css('p::text').get(),
        #     }
        # next_page = response.css('a.next::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, self.parse)

process = CrawlerProcess()
process.crawl(DataCampSpider)
process.start()  # the script will block here until the crawling is finished
    
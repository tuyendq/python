import scrapy
from scrapy.crawler import CrawlerProcess

class YoutubeSpider(scrapy.Spider):
    name = "youtube_spider"

    def start_requests(self):
        urls = [
            'https://www.practicehabits.net',
            # 'https://www.youtube.com/',
            # 'https://www.youtube.com/@summaryversion/videos',
            # 'https://www.youtube.com/c/YourChannelName/videos'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for video in response.css('a#video-title'):
            # yield {
            #     'title': video.css('::text').get(),
            #     'url': response.urljoin(video.attrib['href'])
            # }
        print(response.css('html > title::text').extract())

process = CrawlerProcess()
process.crawl(YoutubeSpider)
process.start()
process.stop()
import scrapy

class YoutubeSpider(scrapy.Spider):
    name = "youtube_spider"
    def start_requests(self):
        allowed_domains = ["youtube.com"]
        urls = ["https://www.youtube.com/@summaryversion/videos"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for video in response.css('a#video-title'):
            yield {
                'title': video.css('::text').get(),
                'link': response.urljoin(video.attrib['href'])
            }
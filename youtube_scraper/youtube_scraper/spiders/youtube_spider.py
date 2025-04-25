import scrapy

class YoutubeSpider(scrapy.Spider):
    name = "youtube_spider"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://www.youtube.com/@summaryversion/videos"]  # Replace with the target channel URL

    def parse(self, response):
        for video in response.css('a#video-title'):
            yield {
                'title': video.css('::text').get(),
                'link': response.urljoin(video.attrib['href'])
            }
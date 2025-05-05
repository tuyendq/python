import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

"""
class YoutubeSpider(scrapy.Spider):
    name = "youtube_spider"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://www.youtube.com/@summaryversion/videos"]  # Replace with the target channel URL

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
        }
        # for video in response.css('a#video-title'):
        #     yield {
        #         'title': video.css('::text').get(),
        #         'link': response.urljoin(video.attrib['href'])
        #     }
"""
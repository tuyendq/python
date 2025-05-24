import scrapy
from scrapy_selenium import SeleniumRequest



class TinhtongVnSpider(scrapy.Spider):
    name = "tinhtong.vn"
    allowed_domains = ["tinhtong.vn"]
    start_urls = ["https://ph.tinhtong.vn/Home/MP3?p=MP3*-+T+Tinh+Van*Cam+Nang+Doi+Nguoi"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                wait_time=15,
                callback=self.parse
            )

    def parse(self, response):
        yield {
        #   "response": response.css("div.mdtc-clnplra-playlist > ul > li")
          "title": response.css("title::text").get(),
          "links": response.css("a::attr(href)").getall()
        #   "links": response.css("div.mdtc-clnplra-playlist > ul > li > a::attr(href)").getall()
        #   "response": response.css("div.mdtc-clnplra-playlist > ul > li > a::text").getall()
      }
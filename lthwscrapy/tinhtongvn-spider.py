import scrapy
from scrapy_selenium import SeleniumRequest
print(scrapy.__version__)

class TinhtongVNSpider(scrapy.Spider):
    name = "tinhtongvn"
    start_urls = ["https://ph.tinhtong.vn/Home/MP3?p=MP3*-+T+Tinh+Van*Cam+Nang+Doi+Nguoi"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=20, wait_until=lambda driver: driver.find_element("xpath", "//div[@class='mdtc-clnplra-playlist']"))

    def parse(self, response):
      yield {
          "response": response.css("div.mdtc-clnplra-playlist > ul > li")
      }
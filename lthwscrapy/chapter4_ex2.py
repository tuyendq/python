def inspect_class(c):
    newc = c()
    meths = dir(newc)
    if 'name' in meths:
        print("Your spider class name is:", newc.name)
    if 'from_crawler' in meths:
        print("It seems you have inherited methods from scrapy.Spider -- NICE!")
    else:
        print("Oh no! It doesn\'t seem that you are inheriting the methods from scrapy.Spider!!")
            


# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
  
# Inspect Your Class
inspect_class(YourSpider)

# Great job setting up a class so that it inherits the tools from scrapy.Spider!


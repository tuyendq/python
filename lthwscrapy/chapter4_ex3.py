
def inspect_class( c ):
    newc = c()
    meths = dir( newc )
    if 'start_requests' in meths:
        print( "The start_requests method yields the following urls:" )
        for u in newc.start_requests():
            print(  "\t-", u )

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com",
    "https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )
    

# Great! We'll discuss more about the start_requests method and how it uses yield in the next lesson.
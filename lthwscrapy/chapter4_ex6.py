def inspect_class( c ):
    newc = c()
    try:
        y = list( newc.start_requests() )
        first_yield = y[0]
        print( "The url you would scrape is:", first_yield.url )
        cb = first_yield.callback
        print( "The name of the callback method you called is:", cb.__name__ )
    except:
       print( "Oh No! Something is wrong with the code! Keep trying." )

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url="https://www.datacamp.com", callback=self.parse )
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )

# Well done! You've been able to use the yielded scrapy.Request to direct to the correct URL and parsing method!
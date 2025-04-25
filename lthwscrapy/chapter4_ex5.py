def inspect_class( c ):
    newc = c()
    try:
        newc.start_requests()
    except:
        print( "Oh No! Something is wrong with the code! Keep trying." )


# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( "Hello World!" )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
# Inspect Your Class
inspect_class( YourSpider )

# Awesome! Self referencing in classes can be a bit confusing, but you nailed it!! (And, don't worry, we don't need to worry too much more about this subject for this course)!!
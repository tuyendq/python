# Import the scrapy library
import scrapy
import requests
from scrapy.http import TextResponse
def inspect_spider( s ):
    news = s()
    try:
        req = list( news.start_requests() )[0]
        url = req.url
        html = requests.get( url ).content
        response = TextResponse( url = url, body = html, encoding = 'utf-8' )
        author_names = req.callback( response )
        print( 'You have collected the author names:')
        for a in author_names:
            print('\t-', a )
    except:
       print( 'Oh no! Something went wrong with the code. Keep trying!')


url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css('p.course-block__author-name::text').extract()
    # Here we will just return the list of Authors
    return author_names
  
# Inspect the spider
inspect_spider( DCspider )


# Nicely done! Notice that you could have written the code for this exercise in the previous chapter, the only difference here is that the response variable appeared within your spider.
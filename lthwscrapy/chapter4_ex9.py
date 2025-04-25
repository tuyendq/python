# Import the scrapy library
import scrapy
import requests
from scrapy.http import TextResponse

def inspect_spider( s ):
    news = s()
    try:
        req1 = list( news.start_requests() )[0]
        html1 = requests.get( req1.url ).content
        response1 = TextResponse( url = req1.url, body = html1, encoding = 'utf-8' )
        req2 = list( news.parse( response1 ) )[0]
        html2 = requests.get( req2.url ).content
        response2 = TextResponse( url = req2.url, body = html2, encoding = 'utf-8' )
        for d in news.parse_descr( response2 ):
            print("One course description you found is:", d )
            break
    except:
        print("Oh no! Something is wrong with the code. Keep trying!")


url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow(url=link, callback=self.parse_descr)
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course-block__description::text' ).extract()
    # For now, just yield the course description
    yield course_descr


# Inspect the spider
inspect_spider( DCdescr )


# That was a long bit of code that you had to read through, but you did it! And you got the crawler, well, crawling!!!
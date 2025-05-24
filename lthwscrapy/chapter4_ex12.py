# Scrapy exercise 12: DataCamp Course Descriptions
def previewCourses( dc_dict, n = 1 ):
  crs_titles = list( dc_dict.keys() )
  print( "A preview of DataCamp Courses:")
  print("----------------------------------------")
  for t in crs_titles[:n]:
    print( "TITLE: %s" % t)
    print("\tDescription: %s" % dc_dict[t] )
    print("")

# Import scrapy
import scrapy
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short, callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url, callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css( 'p.course__description' )
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

# Amazing! As mentioned in the lessons, most of the code you will write for your spider happens in the parsing function(s). Even though you did not have to write much code, please noticed that the code contained in the parsing function(s) is what we've been working to build on throughout this course.
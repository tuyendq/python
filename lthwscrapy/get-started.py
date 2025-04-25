from scrapy import Selector

import requests

url = 'https://quotes.toscrape.com/'
html = requests.get(url).content
sel = Selector(text=html)

print("There are: ", len(sel.xpath('//*')), "elements in the page") 
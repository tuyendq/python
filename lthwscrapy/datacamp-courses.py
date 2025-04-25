from scrapy.http import Response
import requests

url = "https://www.datacamp.com/courses-all/"

# html = requests.get(url).content
# print(html)
# selector = Selector(text=html)
# print(selector.css('head > title::text'))
# print(selector.xpath('/html/head/title/text()'))

# courses = selector.css('div.css-gqd6cf')
# print(len(courses))

response = Response(url=url)

print(response.url)
print(response.status)
print(response.headers)
print(response.body)
# print(response.text)


# list_of_attributes = dir(response)
# for attribute in list_of_attributes:
#     print(attribute)
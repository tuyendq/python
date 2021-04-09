import requests
import re
import xml.etree.ElementTree as ET

# response = requests.get("https://httpbin.org/xml")
# string_xml = response.content
# print(string_xml)
# tree = xml.etree.ElementTree.fromstring(string_xml)
# xml.etree.ElementTree.dump(tree)


url = 'https://sjc.com.vn/xml/tygiavang.xml'

result = requests.get(url)
if result.status_code == 200:
    # print(result.text)
    # tree = ET.parse(result.content)
    # root = tree.getroot()
    # print(tree)
    # print(root)
    # print(root.tag[0].attrib)

    string_xml = result.content
    # print(string_xml)
    # tree = ET.parse(string_xml)
    # print(tree)
    content = ET.fromstring(string_xml)
    # print(type(content))
    # <class 'xml.etree.ElementTree.Element'>
    for child in content:
        print(child.tag, child.text)
    

    children = content.getchildren()
    print(type(children))  # <class 'list'>
    for el in children:
        print(el.text)
    
    print(content[2][0][0].text)
    print(content[2][0][0].attrib)
    
# response_xml_as_string = "xml response string from API"
# responseXml = ET.fromstring(response_xml_as_string)
# testId = responseXml.find('data').find('testId')
# print testId.text


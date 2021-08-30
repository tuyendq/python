# Tutorial from: https://www.edureka.co/blog/web-scraping-with-python/

from bs4 import BeautifulSoup
import pandas as pd
from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from time import sleep


def main():
    """Get what?"""
    options = EdgeOptions()
    options.use_chromium = True
    # options.add_argument("headless")
    # options.add_argument("disable-gpu")
    driver = Edge(options=options)

    # url = 'https://www.flipkart.com/laptops-store'
    url = 'https://podbay.fm/p/sach-noi-danh-cho-ban/'

    driver.get(url)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    el = driver.find_element_by_tag_name('body')
    # el = driver.find_element(By.NAME, "Loading more").send_keys()
    for i in range(4):
        el.send_keys("webdriver" + Keys.END)
        sleep(3)
    # driver.close()

    # print(driver.title)

    # products = []  # List to store name of products
    # prices = []  # List to store price of product
    # ratings = []  # List to store ratings of product
    titles = []
    urls = []

    content = driver.page_source
    # soup = BeautifulSoup(content, 'html.parser')
    soup = BeautifulSoup(content, 'lxml')
    for a in soup.findAll('a', href=True, attrs={'class': 'jsx-1043497740'}):
        # for a in soup.findAll('a', href=True, attrs={'class': 'download'}):
        # name = a.find('div', attrs={'class': 's1Q9rs'})
        # price = a.find('div', attrs={'class': '_30jeq3'})
        # rating = a.find('div', attrs={'class': '_3LWZlK'})
        # products.append(name.text)
        # prices.append(price.text)
        # ratings.append(rating.text)

        # print(a)
        title = a.string
        if title != None:
            print(title)
            titles.append(title)

        link = a.get('href')
        if link.endswith(".mp3"):
            print(link)
            urls.append(link)

    driver.close()
    print(titles)
    print(urls)


if (__name__ == "__main__"):
    main()

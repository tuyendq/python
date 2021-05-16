import sys
import requests as r
from bs4 import BeautifulSoup
import re

site = 'http://chuagiacngo.com/'
# url = 'http://chuagiacngo.com/sach-noi/khi-nao-chim-sat-bay'
# url = 'http://chuagiacngo.com/sach-noi/thay-biet-bay-gio-va-o-day'

def usage():
    """Print usage"""
    print(sys.argv[0], "<url>")
    print("Example:", sys.argv[0], "http://chuagiacngo.com/sach-noi/thay-biet-bay-gio-va-o-day")

def getmp3url(url):
    """Return mp3 url"""
    result = r.get(url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
        # print(soup.find("div", class_ = "jplayer")
        playList = soup.find_all("div", class_ = "jplayer")
        for el in playList:
            # print(el.get('data-jpsrc'))
            return el.get('data-jpsrc')

    #for headline in soup.find_all("data-jpsr
    #    print(headline.text)
    else:
        print("Status code: ",result.status_code)
        return None
def gethref(url):
    """Get all href .mp3 and save to links.txt file"""
    result = r.get(url)
    if result.status_code == 200:
        # print(result.text)
        soup = BeautifulSoup(result.content, "html.parser")
        # all_href = soup.find_all("a")
        # all_href = soup.find_all("a", attrs = {"href": re.compile("^index")})
        all_href = soup.find_all("a", attrs = {"href": re.compile(".mp3$")})
        
        # print(all_href)
        for el in all_href:
            # print(el)
            # print(el.get("href") + "," + el.text)
            link = el.get("href")
            open("links.txt", "a").write(link + "\n")
    else:
        print("Status code: ",result.status_code)
        return None
    
def getFilename(url):
    """Get basename from url"""
    if url.find('/'):
        return url.rsplit('/', 1)[1]

def main():
    # dl_link = getmp3url(url1)
    # print(dl_link)
    
    # result  = r.get(dl_link, allow_redirects=True)
    # print(result.headers)
    # #filename = getFilename(r.headers.get('content-disposition'))
    # fileName = getFilename(dl_link)
    # print("Downloading file...")
    # open(fileName, 'wb').write(result.content)

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    url = sys.argv[1]

    gethref(url)


if __name__ == "__main__":
    main()
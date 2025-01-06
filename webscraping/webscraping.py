import requests as r
from bs4 import BeautifulSoup
import re

siteName = 'http://trungtamhotong.org/'
url = 'http://trungtamhotong.org/index.php?module=phapthoai&cat_id=0&page=1'
url1 = 'http://trungtamhotong.org/index.php?module=phapthoai&function=detail&page=1&id=510'
url2 = 'http://trungtamhotong.org/index.php?module=phapthoai&function=detail&page=1&id=511'


def usage():
    """Print usage"""
    pass

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
    """Get all href"""
    result = r.get(url)
    if result.status_code == 200:
        # print(result.text)
        soup = BeautifulSoup(result.content, "html.parser")
        # all_href = soup.find_all("a")
        all_href = soup.find_all("a", attrs = {"href": re.compile("^index")})
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

def downloadmp3(filename):
    """Download list of mp3 files in a list .txt"""
    with open(filename) as file:
        lines = file.readlines()
    
    count = 0
    for line in lines:
        count = count + 1
        # print(line.strip())
        mp3link = siteName + line.strip()
        print(mp3link)

        dl_link = getmp3url(mp3link)
        print(dl_link)

        mp3Filename = getFilename(dl_link)
        print(mp3Filename)

        print("Downloading file...")
        result  = r.get(dl_link, allow_redirects=True)
        open(mp3Filename, 'wb').write(result.content)

    print("Total lines: ", count)

def main():
    # dl_link = getmp3url(url1)
    # print(dl_link)
    
    # result  = r.get(dl_link, allow_redirects=True)
    # print(result.headers)
    # #filename = getFilename(r.headers.get('content-disposition'))
    # fileName = getFilename(dl_link)
    # print("Downloading file...")
    # open(fileName, 'wb').write(result.content)

    # Get all href in an url
    # gethref(url)

    # Print text file line by line
    downloadmp3("alllinks.txt")

if __name__ == "__main__":
    main()
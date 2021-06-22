import sys
import requests as r

def usage():
    print("Usage: ", sys.argv[0], " <urllinks-line-by-line.txt>")

def getFilename(url):
    """Extract base filename from url"""
    if url.find('/'):
        return (url.rsplit('/', 1)[1]).rstrip()

def downloadmp3(url):
    """Download mp3 file from a url link"""
    print("URL: ", url)
    mp3Filename = getFilename(url)
    print("Start downloading ", mp3Filename, " ...")
    # result = r.get(url, allow_redirects=True, verify=False)
    # result = r.get(url, allow_redirects=True)
    result = r.get(url)
    if result.status_code == 200:    
        print("Header: ", result.headers)
        print("Saving to file: ", mp3Filename)
        open(mp3Filename, 'wb').write(result.content)
        print("Finish downloading ", mp3Filename, " ...")
    else:
        print("Error occurred. Status code: ", result.status_code, result.reason)

def download(filename):
    """Download list of mp3 file in a file, line-by-line"""
    with open(filename) as file:
        for url in file:
            print("Source URL:", url)
            downloadmp3(url)

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    
    download(sys.argv[1])
    

if __name__ == "__main__":
    main()
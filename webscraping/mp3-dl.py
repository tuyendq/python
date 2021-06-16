import sys
import requests as r

def usage():
    print("Usage: ", sys.argv[0], " <urllinks-line-by-line.txt>")

def getFilename(url):
    """Extract base filename from url"""
    if url.find('/'):
        return url.rsplit('/', 1)[1]

def downloadmp3(url):
    """Download mp3 file from a url link"""
    mp3Filename = getFilename(url)
    print("Start downloading ", mp3Filename, " ...")
    result = r.get(url, allow_redirects=True)
    open(mp3Filename, 'wb').write(result.content)
    print("Finish downloading ", mp3Filename, " ...")

def download(filename):
    """Download list of mp3 file in a file, line-by-line"""
    with open(filename) as file:
        for url in file:
            downloadmp3(url)

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    
    download(sys.argv[1])
    

if __name__ == "__main__":
    main()
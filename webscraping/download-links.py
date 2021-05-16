import sys
import requests as r

def usage():
    """Print usage syntax"""
    print(sys.argv[0], "<links.txt>")
    print("links.txt: list of urls to download, line by line")

def getFilename(url):
    """Get basename from url"""
    if url.find('/'):
        return url.rsplit('/', 1)[1]    

def main():
    """"""
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    
    links = sys.argv[1]
    count = 0
    with open(links, 'r') as f:
        while True:
            count = count + 1
            line = f.readline().rstrip("\n")
            if not line:
                break
            print("Line", count, ":", line)
            filename = getFilename(line)
            print("Downloading ", filename)

            result = r.get(line, allow_redirects=True)
            open(filename, 'wb').write(result.content)

if __name__ == "__main__":
    main()


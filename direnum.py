import requests
import sys

directories = open("wordlist.txt", "r").read().splitlines()
target_url = sys.argv[1]
found_dirs = []
for directory in directories:
    response = requests.get(target_url + "/" + directory + ".html")
    if response.status_code == 404:
        pass
    else:
        found_dirs.append(directory)
        print("Found: " + directory)
print("Enumeration complete. Found directories:")
for d in found_dirs:
    print(d)

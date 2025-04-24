# Use Session in requests

from pickle import GLOBAL
import requests

# Create a Session object
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Accept': '*/*'
}
COOKIES_JAR = {}


URL = 'https://httpbin.org/headers'
URL = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"


# 1st Session object
def session_1():
    """1st Session object"""
    print("\n=====1st Session object=====")
    global HEADERS
    global COOKIES_JAR
    s = requests.Session()
    # s.headers.update({'accept':'tuyen', 'User-Agent':'powershell'})
    s.headers.update(HEADERS)
    resp = s.get(URL)
    # print(resp.text)
    print(s.headers)
    HEADERS = s.headers.copy()
    COOKIES_JAR = s.cookies.copy()
    print("headers:\n", HEADERS)
    print("COOKIES_JAR:\n", COOKIES_JAR)
    print("s.cookies:\n", s.cookies)

# 2nd Session object
def session_2():
    """2nd Session object"""
    print("\n=====2nd Session object=====")
    global HEADERS
    global COOKIES_JAR
    s2 = requests.Session()
    s2.headers.update(HEADERS)
    s2.cookies.update(COOKIES_JAR)
    resp2 = s2.get(URL)
    print("headers:\n", s2.headers)

    print("cookies:\n", s2.cookies)

if __name__ == "__main__":
    session_1()

    session_2()
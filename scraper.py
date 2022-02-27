import requests
from bs4 import BeautifulSoup

def parse_web(url,headers=None,raw=False):
    page = requests.get(url,headers=headers).content
    if raw:
        return page
    return BeautifulSoup(page, "html.parser")

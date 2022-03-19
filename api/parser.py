import requests
from lxml import etree

from auth import make_cookies, make_header

def parse_doc(res: requests.Response):
    return etree.HTML(res.text)

def get_doc(se: requests.Session, url: str):
    return parse_doc(se.get(url,
        headers = make_header(),
        cookies = make_cookies()
    ))
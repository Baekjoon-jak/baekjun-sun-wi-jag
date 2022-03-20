import requests
from lxml import etree

from auth import make_cookies, make_header

def parse_doc(res: requests.Response):
    return etree.HTML(res.text)

def get_doc(se: requests.Session, url: str) -> any or None:
    '''GET를 요청하고 결과를 HTML 파싱합니다.
    Return: OK가 아닐시 None를 리턴합니다.
    '''
    res = se.get(url,
        headers = make_header(),
        cookies = make_cookies()
    )
    return parse_doc(res) if res.status_code == 200 else None

def inner_text(tag):
    return (tag.text or '') + ''.join(inner_text(e) for e in tag) + (tag.tail or '')
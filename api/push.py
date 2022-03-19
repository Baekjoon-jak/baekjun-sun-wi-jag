from typing import Literal
import requests
from auth import make_cookies, make_header

from api.parser import get_doc

def get_csrf_key(session: requests.Session, problem_id: int) -> str:
    '''세션의 csrf key를 가져옵니다.'''
    doc = get_doc(session, f"https://www.acmicpc.net/submit/{problem_id}")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]


def solving_submit(session: requests.Session, problem_id: int, code_open: Literal['open', 'close', 'onlyaccepted'], source: str, lang: int) -> bool:
    '''문제 답을 제출합니다.'''
    res = session.post(f"https://www.acmicpc.net/submit/{problem_id}", 
        headers = make_header(),
        cookies = make_cookies(),
        data = {
            "problem_id": problem_id,
            "language": lang,
            "code_open": code_open,
            "source": source,
            "csrf_key": get_csrf_key(session, problem_id)
        }
    )
    return f"/submit/{problem_id}" not in res.url
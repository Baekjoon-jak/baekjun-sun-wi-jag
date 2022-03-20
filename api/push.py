from typing import Literal
import requests
from api.csrf import get_csrf_key
from api.lang import langChk
from auth import make_cookies, make_header

def solving_submit(session: requests.Session, problem_id: int, code_open: Literal['open', 'close', 'onlyaccepted'], source: str, lang: str) -> bool:
    '''문제 답을 제출합니다.'''
    res = session.post(f"https://www.acmicpc.net/submit/{problem_id}", 
        headers = make_header(),
        cookies = make_cookies(),
        data = {
            "problem_id": problem_id,
            "language": langChk(lang),
            "code_open": code_open,
            "source": source,
            "csrf_key": get_csrf_key(session, problem_id)
        }
    )
    return f"/submit/{problem_id}" not in res.url

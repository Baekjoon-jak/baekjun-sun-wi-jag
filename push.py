from typing import Literal
import requests
from auth import make_cookies, make_header

from parse import get_doc

session = requests.Session()

def get_csrf_key() -> str:

    #세션의 csrf key를 가져옵니다.

    doc = get_doc(session, "https://www.acmicpc.net/submit/1000")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]

def solving_submit(problem_id: int, code_open: Literal['open', 'close', 'onlyaccepted'], source: str, lang: int) -> str:

    # 문제 답을 제출합니다.

    res = session.post(f"https://www.acmicpc.net/submit/{problem_id}", 
        headers = make_header(),
        cookies = make_cookies(),
        data = {
            "problem_id": problem_id,
            "language": lang,
            "code_open": code_open,
            "source": source,
            "csrf_key": get_csrf_key()
        }
    )
    if f"/submit/{problem_id}" not in res.url:
        return f"성공 : {res.url}"
    else:
        return f"실패 : {res.text}"



def get_code(source_id: int) -> str:
    res = session.get(f"https://www.acmicpc.net/source/{source_id}", 
        headers = make_header(),
        cookies = make_cookies()
    )
    if f"/source/{source_id}" not in res.url:
        return f"성공 : {res.url}"
    else:
        return f"실패 : {res.text}"



# print(solving_submit(10998, 'close', '''
# a, b = input().split()
# print(int(a)*int(b))
# ''', 28))

print(get_code(16270136))

session.close()
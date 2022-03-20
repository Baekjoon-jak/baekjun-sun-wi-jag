from typing import NamedTuple
from bs4 import BeautifulSoup
import requests
from api.parser import get_doc, inner_text
from auth import make_cookies, make_header
from utils import to_int

class ProblemSolving(NamedTuple):
    problem_id: int or None
    problem_title: str
    source: str
    user: str
    result: str
    memory_used: int or None
    running_time: int or None
    language: str
    code_length: int or None
    sub_time: int


def get_problem_solving(session: requests.Session, solve_id: int) -> ProblemSolving or None:
    '''문제 해결 머시기 가져옴.
    Return: 가져오기 실패 시 None를 리턴합니다.
    '''
    doc = get_doc(session, f"https://www.acmicpc.net/source/{solve_id}")
    if (doc == None): return None

    tr = doc.xpath('//table[@class="table table-striped"]/tbody/tr/td')
    return {
        "problem_id": int(inner_text(tr[2])),
        "problem_title": inner_text(tr[3]),
        "source": inner_text(doc.xpath('//textarea[@name="source"]')[0]),
        "user": inner_text(tr[1]),
        "result": inner_text(tr[4]),
        "memory_used": to_int(tr[5].text),
        "running_time": to_int(tr[6].text),
        "language": tr[7].text,
        "code_length": to_int(tr[8].text),
        "sub_time": to_int(tr[9][0].attrib['data-timestamp'])
    }

# 성공시 코드 및 문제 번호, 실패시 None 반환
def get_code(session: requests.Session, source_id: int) -> str:
    res = session.get(f"https://www.acmicpc.net/source/{source_id}",
        headers = make_header(),
        cookies = make_cookies()
    )
    if res.status_code == 200:
        print("status_code: 200")
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        if soup.find("span", "result-ac"):
            code = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > textarea")
            problem_id = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(8) > div > table > tbody > tr > td:nth-child(3) > a")
            lang = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(8) > div > table > tbody > tr > td:nth-child(8)")
            return {"code": code.text, "problem_id": problem_id.text, "lang": lang.text}
    else:
        print(f"status code: {res.status_code}")

    return None
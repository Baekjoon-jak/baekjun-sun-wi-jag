import requests
from auth import make_cookies, make_header
from bs4 import BeautifulSoup

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
            print("WA")
    else:
        print(f"status code: {res.status_code}")

    return None
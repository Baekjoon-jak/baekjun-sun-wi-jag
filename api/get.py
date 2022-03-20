import requests
from auth import make_cookies, make_header
from bs4 import BeautifulSoup


def get_code(session: requests.Session, source_id: int) -> str:
    res = session.get(f"https://www.acmicpc.net/source/{source_id}",
        headers = make_header(),
        cookies = make_cookies()
    )
    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        code = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > textarea")
        print(code.text)

    else:
        print(f"status code: {res.status_code}")
    return code.text
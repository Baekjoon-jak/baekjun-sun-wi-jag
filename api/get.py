import requests
from auth import make_cookies, make_header


def get_code(session: requests.Session, source_id: int) -> str:
    res = session.get(f"https://www.acmicpc.net/source/{source_id}", 
        headers = make_header(),
        cookies = make_cookies()
    )
    if f"/source/{source_id}" not in res.url:
        return f"성공 : {res.url}"
    else:
        return f"실패 : {res.text}"
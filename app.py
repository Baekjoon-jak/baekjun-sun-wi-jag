from dotenv import load_dotenv
load_dotenv(verbose=True)

# auth는 load_dotenv 아래에 있어야함.
from auth import make_cookies, make_header

import requests

session = requests.Session()


def get_code(source_id: int) -> str:
    res = session.get(f"https://www.acmicpc.net/source/{source_id}", 
        headers = make_header(),
        cookies = make_cookies()
    )
    if f"/source/{source_id}" not in res.url:
        return f"성공 : {res.url}"
    else:
        return f"실패 : {res.text}"


# solving_submit(10998, 'close', '''
# a, b = input().split()
# print(int(a)*int(b))
# ''', 28)

print(get_code(16270136))

session.close()
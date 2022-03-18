from typing import Literal
import requests
from auth import make_cookies, make_header

from parse import get_doc

session = requests.Session()

def get_csrf_key() -> str:
    '''
    세션의 csrf key를 가져옵니다.
    '''
    doc = get_doc(session, "https://www.acmicpc.net/submit/1000")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]

def solving_submit(problem_id: int, code_open: Literal['open', 'close', 'onlyaccepted'], source: str, lang: int) -> bool:
    '''
    문제 답을 제출합니다.

    Args:
        lang: 
            84 C++17,
            28 Python 3,
            73 PyPy3,
            0 C99,
            93 Java 11,
            68 Ruby,
            69 Kotlin (JVM),
            74 Swift,
            58 Text,
            86 C#,
            17 Node.JS,
            12 Go,
            29 D,
            94 Rust 2018,
            85 C++17 (Clang)
    '''
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
    return f"/submit/{problem_id}" not in res.url


print(solving_submit(10998, 'close', '''
#include<stdio.h>

int main()
{
	int A, B;
	scanf("%d %d", &A, &B);

	printf("%d", A * B);

	return 0;
}''', 0))

session.close()
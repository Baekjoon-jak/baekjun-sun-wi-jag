import enum
from multiprocessing.pool import CLOSE
from typing import Literal
import requests

from parse import get_doc, post_doc

session = requests.Session()

def get_csrf_key() -> str:
    '''
    세션의 csrf key를 가져옵니다.
    '''
    doc = get_doc(session, "https://www.acmicpc.net/submit/1000")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]


def psolving_submit(problem_id: int, code_open: Literal['open', 'close', 'onlyaccepted'], source: str, lang: int):
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
    post_doc(session, f"https://www.acmicpc.net/submit/{problem_id}", {
        "problem_id": problem_id,
        "language": lang,
        
    })

session.close()
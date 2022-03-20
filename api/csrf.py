
import requests
from api.parser import get_doc, inner_text

def get_csrf_key(session: requests.Session, problem_id: int) -> str:
    '''세션의 csrf key를 가져옵니다.'''
    doc = get_doc(session, f"https://www.acmicpc.net/submit/{problem_id}")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]
import requests
from lxml import etree


from api.parser import get_doc, inner_text

def get_csrf_key(session: requests.Session, problem_id: int) -> str:
    '''세션의 csrf key를 가져옵니다.'''
    doc = get_doc(session, f"https://www.acmicpc.net/submit/{problem_id}")
    return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]

def get_problem_solving(session: requests.Session, solve_id: int):
  '''문제 해결 머시기 가져옴'''
  doc = get_doc(session, f"https://www.acmicpc.net/source/{solve_id}")
  print(inner_text(doc.xpath('//textarea[@name="source"]')[0]))
import requests

from parse import get_doc, post_doc

session = requests.Session()

def get_csrf_key() -> str:
  doc = get_doc(session, "https://www.acmicpc.net/source/16270136")
  return doc.xpath('//*[@name="csrf_key"]')[0].attrib["value"]

session.close()
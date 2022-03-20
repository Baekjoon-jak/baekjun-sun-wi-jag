import os
import time
from dotenv import load_dotenv
from api.lang import code_to_lang
from api.submit import solving_submit
import requests
from api.user import get_user_info

from autobaek import get_sources
from salt.code_salt import source_code_salting

load_dotenv(verbose=True)
session = requests.Session()


def read_file(path: str) -> str:
  file = open(path, "r")
  strings = file.read()
  file.close()
  return strings


src_folder = input('소스파일 폴더: ')
sources = get_sources(src_folder)
solved_problems = get_user_info(session, os.getenv('USER_NAME'))["solved_problems"]

for lang_code, source in sources.items():
  print(f'푸시 할 언어: {code_to_lang(lang_code)}')

  for problem_id, src_dir in source.items():
    if problem_id in solved_problems:
      print(f'이미 해결된 문제: {problem_id}')
      continue
    try:  
      src = read_file(src_dir)
      print(f'문제: {problem_id}\n  --  소스  --  \n{src}\n  --  소스  --  ')

      src = source_code_salting(src)
      
      solving_submit(session, problem_id, 'close', src, lang_code)
    except Exception as e:
      print(f'푸시 실패 {e}')
      continue

    time.sleep(10)

session.close()
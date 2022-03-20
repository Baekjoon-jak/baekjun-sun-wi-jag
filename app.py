from dotenv import load_dotenv
from api.get import get_code, get_problem_solving
from api.lang import lang_to_code
from api.submit import solving_submit
import requests

load_dotenv(verbose=True)
# auth는 load_dotenv 아래에 있어야함.

<<<<<<< HEAD
session = requests.Session()

for i in range(13000000, 350000, -1):
  result = get_code(session, i)
  if result != None:
    if solving_submit(session, result["problem_id"], 'open', result["code"], result["lang"]):
      print("🚀 성공")
      print(f"https://www.acmicpc.net/status?problem_id={result['problem_id']}")
    else:
      print("❗ 실패")
  else:
    print("❗ 실패")
=======

session = requests.Session()

print(get_problem_solving(session, 17280484))

# result = get_code(session, 16270141)
# if result != None:

#   if solving_submit(session, result["problem_id"], 'open', result["code"], lang_to_code(result["lang"])):
#     print("🚀 성공")
#     print(f"https://www.acmicpc.net/status?problem_id={result['problem_id']}")
#   else:
#     print("❗ 실패")
# else:
#   print("❗ 실패")
>>>>>>> 43f302063bd43e06e15a218155e4db71f35ae3a3

session.close()
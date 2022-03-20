from dotenv import load_dotenv
from api.get import get_code, get_problem_solving
from api.lang import lang_to_code
from api.submit import solving_submit
import requests

load_dotenv(verbose=True)
# auth는 load_dotenv 아래에 있어야함.


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

session.close()
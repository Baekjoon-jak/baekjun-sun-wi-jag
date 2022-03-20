from dotenv import load_dotenv
from api.get import get_code
import requests

load_dotenv(verbose=True)
# auth는 load_dotenv 아래에 있어야함.

from auth import make_cookies, make_header

session = requests.Session()


get_code(session,16270141) #16270141, 16270136


session.close()
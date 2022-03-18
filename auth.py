from dotenv import load_dotenv
import os

def make_header():
    return {
        "referer": "https://www.acmicpc.net/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
        "authority": "www.acmicpc.net"
    }

def make_cookies():
   

    load_dotenv(verbose=True)

    return {
        "bojautologin": os.getenv('AUTO_LOGIN')
    }
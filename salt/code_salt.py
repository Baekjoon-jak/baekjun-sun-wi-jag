
import random

def source_code_salting(src: str, salt: int = 3) -> str:
    '''소스코드에 간을 칩니다.'''
    rn = random.randint(0, salt)
    return ('\n' * rn) + src + ('\n' * (salt - rn))


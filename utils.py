
def to_int(st: str, default: int or None = None) -> int or None:
    try:
        return int(st)
    except:
        return default

def try_get(a, i, default = None) -> any or None:
    try:
        return a[i]
    except:
        return default
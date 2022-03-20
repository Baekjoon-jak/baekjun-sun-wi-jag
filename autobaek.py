
import os

from api.lang import code_to_lang

def get_sources(folder: str) -> dict[int, dict[int, str]]:
    lsrc = {}
    for dir in os.listdir(folder):
        lang_code = int(os.path.basename(dir))
        dir = os.path.join(folder, dir)
        codes = {}
        
        for file in os.listdir(dir):
            id = int(os.path.splitext(file)[0])
            codes[id] = os.path.join(dir, file)

        print(f'언어: {code_to_lang(lang_code)}, 문제갯수: {len(codes)}, 문제: ' + ', '.join(str(k) for k, _ in codes.items()))
        lsrc[lang_code] = codes
    return lsrc

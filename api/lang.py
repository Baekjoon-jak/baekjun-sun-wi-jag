BaekJoonLanguages = {
    "C++17": 84,
    "C++14": 84, #확실하지 않음
    "C++98": 84, #확실하지 않음
    "Python 3": 28,
    "Python 2": 28, #확실하지 않음
    "PyPy3": 73,
    "C99": 0,
    "Java": 11,
    "Java 8": 11, #확실하지 않음
    "Java 11": 11, #확실하지 않음
    "Ruby": 68,
    "Kotlin (JVM)": 69,
    "Swift": 74,
    "Text": 58,
    "C#": 86,
    "C# 6.0 (Mono)": 86, #확실하지 않음
    "Node.JS": 17,
    "Go": 12,
    "D": 29,
    "Rust 2018": 94,
    "C++17 (Clang)": 85
}

def lang_to_code(lang: str):
    return BaekJoonLanguages[lang]



word = "cable"
first = "a"
second = "b"

def goes_after(word: str, first: str, second: str):
    return False if word.find(first + second) < 0 else True

print(goes_after(word, first, second))
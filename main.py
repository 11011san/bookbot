def main():
    text = get_text("books/frankenstein.txt")
    print(f"There was {word_count(text)} words in this file")
    print(f"Chars fequense:")
    print(count_char(text))

def word_count(text):
    return len(text.split())

def count_char(text):
    dic = {}
    for ch in text.lower():
        dic[ch] = dic.setdefault(ch, 0) + 1
    return dic


def get_text(path):
    with open(path) as f:
        return f.read()

main()
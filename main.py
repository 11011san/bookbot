import re


def main(path):
    text = get_text(path)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(text)} words found in the document")
    print(f"")
    print_char_frequency(text)
    print(f"--- End report ---")

def word_count(text):
    return len(text.split())

def count_char(text):
    dic = {}
    for ch in text.lower():
        dic[ch] = dic.setdefault(ch, 0) + 1
    return dic

def print_char_frequency(text):
    dic = count_char(text)
    list = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    for ch, freq in list:
        if ch.isalpha():
            print(f"The '{ch}' character was found {freq} times")

def get_text(path):
    with open(path) as f:
        return f.read()

main("books/frankenstein.txt")
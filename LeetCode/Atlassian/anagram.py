from collections import Counter


def countCharacters(words, chars: str) -> int:
    a = Counter(chars)
    c = 0
    for word in words:
        if Counter(word) -a == Counter():
            c += len(word)
    return c

print(countCharacters(["cat","bt","hat","tree"], "atach"))
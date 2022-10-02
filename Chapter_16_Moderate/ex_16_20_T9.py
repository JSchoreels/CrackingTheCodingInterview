from typing import List


def char_to_digit_t9(char : str):
    return {
        'a' : 2,
        'b' : 2,
        'c' : 2,
        'd' : 3,
        'e' : 3,
        'f' : 3,
        'g' : 4,
        'h' : 4,
        'i' : 4,
        'j' : 5,
        'k' : 5,
        'l' : 5,
        'm' : 6,
        'n' : 6,
        'o' : 6,
        'p' : 7,
        'q' : 7,
        'r' : 7,
        's' : 7,
        't' : 8,
        'u' : 8,
        'v' : 9,
        'w' : 9,
        'x' : 9,
        'y' : 9,
        'z' : 9
    }[char]

dict_t9 = {}

def store_word(word : str):
    n = len(word)
    result = 0
    for char in word:
        result += char_to_digit_t9(char) * 10**(n-1)
        n -= 1
    if result in dict_t9:
        dict_t9[result].append(word)
    else:
        dict_t9[result] = [word]


def store_words(words : List[str]):
    for word in words:
        store_word(word)

store_words(['tree', 'car', 'used'])


def t9(code):
    return dict_t9[code]

print(t9(8733))
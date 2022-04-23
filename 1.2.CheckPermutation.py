# 1.2 : Given two strings, write a method to decide if one is a permutation of the other


def permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    histo_string1 = {}
    for char in string1:
        if char not in histo_string1:
            histo_string1[char] = 1
        else:
            histo_string1[char] += 1
    for char in string2:
        if char not in histo_string1:
            return False
        else:
            if histo_string1[char] <= 0:
                return False
            histo_string1[char] -= 1
    return True

def permutation_latin_lower(string1, string2):
    if len(string1) != len(string2):
        return False
    histo_string1 = [0] * 26
    for char in string1:
        char_pos = ord(char) - ord('a')
        histo_string1[char_pos] += 1
    for char in string2:
        char_pos = ord(char) - ord('a')
        if histo_string1[char_pos] <= 0:
            return False
        histo_string1[char_pos] -= 1
    return True



implementations = [permutation_latin_lower]

for implementation in implementations:
    for valid in [("abcde", "edcba"), ("", "")]:
        assert implementation(*valid)
    for invalid in [("ab", "aa"), ("", "a"), ("a", "")]:
        assert not implementation(*invalid)
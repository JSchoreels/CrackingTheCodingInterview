# 1.1 Is Unique : Implement an algorithm to determine if a string has all unique characters, what if you cannot use additional structure

valids = ["abcde", "ab", "a", ""]
invalids = ["aa", "aba", "abcdbe"]

def is_unique_naive(string):
    for (i, char) in enumerate(string):
       if char in string[:i] or char in string[i+1:]:
           return False
    return True

def is_unique_dict(string):
    occurences = {}
    for char in string:
        if char not in occurences:
            occurences[char] = 1
        else:
            return False
    return True

def is_unique_sort(string):
    sorted_string = sorted(string)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True


implementations = [is_unique_naive, is_unique_dict, is_unique_sort]

for implementation in implementations:
    for valid in valids:
        assert implementation(valid)
    for invalid in invalids:
        assert not implementation(invalid)
def group_anagrams(arr):
    result_dict = {}
    for string in arr:
        signature = create_signature(string)
        if signature in result_dict:
            result_dict[signature].append(string)
        else:
            result_dict[signature] = [string]
    result_arr = []
    for signature in result_dict:
        result_arr.extend(result_dict[signature])
    return result_arr


def create_signature(word : str):
    word = word.lower()
    histo = [0] * 26
    for char in word:
        histo[ord(char) - ord('a')] += 1
    return ''.join([f"{count}{chr(char)}" for (char, count) in enumerate(histo) if count>0 ])


result = group_anagrams(["test", "testa", "tset", "testa", "testc"])
print(result)
assert result == ['test', 'tset', 'testa', 'testa', 'testc']
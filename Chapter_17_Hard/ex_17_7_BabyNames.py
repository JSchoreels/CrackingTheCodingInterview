from typing import List, Tuple


def get_key_if_exist(name, dict):
    if name in dict:
        return dict[name]
    return None

def build_synonyms_dict(synonyms : List[Tuple[str, str]]):
    synonyms_dict = {}
    for syno in synonyms:
        key1 = get_key_if_exist(syno[0], synonyms_dict)
        key2 = get_key_if_exist(syno[1], synonyms_dict)
        if key1 and key2:
            if key1 == key2: # Everything is ok
                pass
            else: # Need to resync all key2 to key1
                for name,key in synonyms_dict.items():
                    if key == key2:
                        synonyms_dict[name] = key1
        elif key1 and not key2:
            synonyms_dict[syno[1]] = key1
        elif not key1 and key2:
            synonyms_dict[syno[0]] = key2
        else:
            synonyms_dict[syno[0]] = syno[0]
            synonyms_dict[syno[1]] = syno[0]
    return synonyms_dict

def baby_names(names : List[Tuple[str, int]], synonyms : List[Tuple[str, str]]):
    synonyms_dict = build_synonyms_dict(synonyms)
    frequencies = {}
    for names, count in names:
        frequencies[synonyms_dict[names]] = frequencies.get(synonyms_dict[names], 0) + count
    return frequencies

names = [("John",15), ("Jon",12), ("Jojo",1), ("Chris",13), ("Kris",4), ("Christopher",19)]
synonyms = [("Jon", "John"), ("Jojo", "Johnny"), ("John", "Jojo"), ("Chris", "Kris"), ("Chris", "Christopher")]
result = baby_names(names, synonyms)
print(result)
assert result == {'Jon': 28, 'Chris': 36}
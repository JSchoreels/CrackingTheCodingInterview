from string import punctuation
from typing import List



def get_frequencies(lines : List[str]):
    histo = {}
    for line in lines:
        line = line.strip().lower().translate(line.maketrans('','', punctuation))
        for word in line.split(' '):
            word = word.lower()
            if word not in histo:
                histo[word] = 1
            else:
                histo[word] += 1
    return histo


frequencies = get_frequencies(["Chapiter 1", "This book is about some fantasy", "and about many other things outside fantasy."])
print(frequencies)
assert frequencies["fantasy"] == 2
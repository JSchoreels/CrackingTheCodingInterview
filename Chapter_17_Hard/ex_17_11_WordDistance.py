from typing import List


def word_distance(book: List[str], word1, word2):
    word1_pos = None
    word2_pos = None
    min_dist = None
    for i in range(len(book)):
        if book[i] == word1:
            word1_pos = i
        elif book[i] == word2:
            word2_pos = i
        if word1_pos and word2_pos and (not min_dist or abs(word1_pos - word2_pos) < min_dist):
            min_dist = abs(word1_pos - word2_pos)
    return min_dist

def create_pos_map(book: List[str]):
    map = {}
    for i in range(len(book)):
        map.setdefault(book[i], []).append(i)
    return map

def word_distance_with_pos(pos, word1, word2):
    assert word1 in pos and word2 in pos
    pos_word1 = pos[word1]
    pos_word2 = pos[word2]
    i_1 = 0
    i_2 = 0
    min_dist = max(pos_word1[-1], pos_word2[-1])
    while i_1 < len(pos_word1) and i_2 < len(pos_word2):
        cand_min_dist = abs(pos_word1[i_1] - pos_word2[i_2])
        if cand_min_dist < min_dist:
            min_dist = cand_min_dist
        if pos_word1[i_1] < pos_word2[i_2]:
            i_1 += 1
        elif pos_word2[i_2] < pos_word1[i_1]:
            i_2 += 1
        else:
            return 0
    return min_dist


book = "AXXXXXBXXXXAXXBXXXXXXAXXXXXXXXB"
word1 = "A"
word2 = "B"
print(word_distance(list(book), word1, word2))
print(word_distance(list(book), word2, word1))
pos = create_pos_map(book)
print(word_distance_with_pos(pos, word1, word2))
print(word_distance_with_pos(pos, word2, word1))
print(pos)
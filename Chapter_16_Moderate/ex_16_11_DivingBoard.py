# 16.11 Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
# There are two types of planks, one of length shorter and one of length longer. You must use
# exactly K planks of wood. Write a method to generate all possible lengths for the diving board


def diving_board(shorter, longer, K):
    def length_diving_board(n_shorter):
        return n_shorter * shorter + (K - n_shorter) * longer

    possibilities = set()
    for n in range(0, K):
        possibilities.add(length_diving_board(n))
    return possibilities


result = diving_board(1, 5, 5)
print(result)
assert {9, 13, 17, 21, 25} == result
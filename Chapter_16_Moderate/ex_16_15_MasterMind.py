# 16.15 Master Mind
from enum import IntEnum
from typing import List


class Color(IntEnum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4

def master_mind(actual : List[IntEnum], expected : List[IntEnum]):
    expected_ocurrences = {}
    actual_occurences = {}
    hits = 0
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        if actual[i] == expected[i]:
            hits += 1
        else:
            expected_ocurrences[expected[i]] = expected_ocurrences.get(expected[i], 0) + 1
            actual_occurences[actual[i]] = actual_occurences.get(actual[i], 0) + 1
    pseudo_hits = 0
    for color, count in enumerate(expected_ocurrences):
        if color in actual_occurences:
            pseudo_hits += min(count, actual_occurences[color])
    return hits, pseudo_hits

print(master_mind([Color.RED, Color.RED, Color.YELLOW, Color.BLUE],
                  [Color.RED, Color.YELLOW, Color.RED, Color.GREEN]))
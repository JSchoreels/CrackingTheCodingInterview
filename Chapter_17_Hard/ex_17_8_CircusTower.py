from typing import List


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


def longest_finishing_at(at, weights, longest_finishing_at_memo):
    result_size = 1
    result_sequence = [weights[at]]
    for i in range(at):
        prefix_size, prefix_sequence = longest_finishing_at_memo[i]
        if prefix_sequence[-1] < weights[at] and prefix_size >= result_size:
            result_size = prefix_size + 1
            result_sequence = prefix_sequence + [weights[at]]
    longest_finishing_at_memo[at] = (result_size, result_sequence)
    return result_size, result_sequence



def longest_increasing_sequence(weights):
    longest_size = 0
    longest_sequence = []
    longest_finishing_at_memo = [None] * len(weights)
    for i in range(len(weights)):
        candidate_longest_size, candidate_longest_sequence = longest_finishing_at(i, weights, longest_finishing_at_memo)
        if candidate_longest_size > longest_size:
            longest_size = candidate_longest_size
            longest_sequence = candidate_longest_sequence
    return longest_size, longest_sequence


def circus_tower(people: List[Person]):
    people.sort(key=lambda p: -p.height)
    weight = list(map(lambda p: p.weight, people))
    return longest_increasing_sequence(weight)


print(circus_tower([Person(200, 13), Person(180, 10), Person(190, 14), Person(170, 11), Person(160, 12)]))

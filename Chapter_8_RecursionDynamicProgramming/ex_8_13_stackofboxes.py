from __future__ import annotations

class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def is_valid_base(self, top_box : Box):
        return self.width > top_box.width \
               and self.height > top_box.height \
               and self.depth and self.depth > top_box.depth

    def __repr__(self):
        return f"({self.width},{self.height},{self.depth})"


def tallest_possible_stack(boxes : list[Box]):
    memo = [None] * len(boxes)
    def tallest_possible_stack_rec(start):
        if len(boxes) == start:
            return [], 0
        elif len(boxes) == start-1:
            return [boxes[start]], boxes[start].height
        else:
            if memo[start]:
                print(f'[CACHE] tallest for input {boxes[start:]} : {memo[start][0]} with height {memo[start][1]}')
                return memo[start]
            base_candidate = boxes[start]
            tallest = [base_candidate]
            max = base_candidate.height
            for next_candidate_index in range(start+1, len(boxes)):
                rest_tallest, rest_max = tallest_possible_stack_rec(next_candidate_index)
                if len(rest_tallest) > 0 and base_candidate.is_valid_base(rest_tallest[0]) and base_candidate.height+rest_max > max:
                    tallest = [base_candidate]
                    tallest.extend(rest_tallest)
                    max = base_candidate.height + rest_max
            print(f'tallest for input {boxes[start:]} : {tallest} with height {max}')
            memo[start] = tallest, max
            return tallest, max

    tallest_starting_from_any, max_from_any = tallest_possible_stack_rec(0)
    for i in range(1, len(boxes)):
        tallest_starting_from_i, max_from_i = tallest_possible_stack_rec(i)
        if max_from_i > max_from_any:
            max_from_any = max_from_i
            tallest_starting_from_any = tallest_starting_from_i
    return tallest_starting_from_any, max_from_any


boxes = [
    Box(6,9,3),
    Box(6,8,5),
    Box(4,7,4),
    Box(5,4,5),
    Box(3,3,4),
    Box(1,1,4),
    Box(4,5,2),
    Box(3,5,1)
]
boxes.sort(key = lambda b : -b.height)
print(tallest_possible_stack(boxes))
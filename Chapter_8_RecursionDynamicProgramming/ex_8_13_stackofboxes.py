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


def tallest_possible_stack(boxes : list[Box]):
    if len(boxes) == 0:
        return [], 0
    elif len(boxes) == 1:
        return boxes[0], boxes[0].height
    else:
        tallest, max = [], 0
        for base_candidate in boxes:
            rest_boxes = boxes.copy()
            rest_boxes.remove(base_candidate)
            rest_tallest, rest_max = tallest_possible_stack(rest_boxes)
            if base_candidate.is_valid_base(rest_tallest[0]) and rest_max > max:
                tallest = [base_candidate]
                tallest.extend(rest_tallest)
                max = base_candidate.height + rest_max
        return tallest, max


boxes = [

]
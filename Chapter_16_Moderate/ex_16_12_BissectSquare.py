import matplotlib.pyplot


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x},{self.y}"


class Square:
    def __init__(self, top_left, length):
        self.top_left: Point = top_left
        self.length = length

    def get_center(self):
        return Point(
            self.top_left.x + self.length / 2,
            self.top_left.y + self.length / 2
        )


class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def __repr__(self):
        return f"y={self.slope}x+{self.intercept}"


def bissect_square(sq1: Square, sq2: Square):
    c1 = sq1.get_center()
    c2 = sq2.get_center()
    return Line(
        slope := (c2.y - c1.y) / (c2.x - c1.x),
        c1.y - slope * c1.x
    )


sq1 = Square(Point(0, 5), 2)
print(sq1.get_center())
sq2 = Square(Point(5, 1), 4)
print(sq2.get_center())
print(bissect_square(sq1, sq2))

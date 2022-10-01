# 16.14 Best Line: Given a two-dimensional graph with points on it, find a line which passes the most
# number of points.
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(f"{self.x},{self.y}")

    def __repr__(self):
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def from_intercept(p1: Point, p2: Point):
        self = Line(0,0)
        if p1 == p2:
            raise ValueError("Infinite number of lines passing through p1 and p2 if p1=p2")
        if abs(p1.x - p2.x) < 1e-8:
            self.slope = "inf"
            self.intercept = p1.y
        else:
            self.slope = (p1.y - p2.y) / (p1.x - p2.x)
            self.intercept = p1.y - self.slope * p1.x
        return self

    def id(self):
        if self.slope == "inf":
            return f"inf-{self.intercept}"
        return f"{round(self.slope, 5)}-{self.intercept}"

    def __repr__(self):
        return self.id()

    def __hash__(self):
        return hash(self.id())

    def __eq__(self, other):
        return self.id() == other.id()


def best_line(points: List[Point]):
    lines = {}
    max_encountered = 0
    max_encountered_line = None
    for i_src in range(len(points)):
        src = points[i_src]
        for i_dst in range(i_src+1, len(points)):
            dst = points[i_dst]
            line = Line.from_intercept(src, dst)
            points_intersected = lines.get(line, set())
            points_intersected.add(src)
            points_intersected.add(dst)
            new_encountered_counter = len(points_intersected)
            lines[line] = points_intersected
            if new_encountered_counter > max_encountered:
                max_encountered = new_encountered_counter
                max_encountered_line = line
    print(lines)
    return max_encountered_line

print(best_line(
    [
        Point(1,1),
        Point(2,2),
        Point(3,3),
        Point(2,0),
        Point(3,0),
        Point(4,0),
        Point(5,0),
        Point(2,1),
    ]
))
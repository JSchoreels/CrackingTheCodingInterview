class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x,self.y})"

class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_m(self):
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def get_p(self):
        return self.end.y - self.get_m() * self.end.x

    def get_dom(self):
        return min(self.start.x, self.end.x), max(self.start.x, self.end.x)

    def get_img(self):
        return min(self.start.y, self.end.y), max(self.start.y, self.end.y)

    def is_in_dom(self, x: float):
        return self.get_dom()[0] <= x <= self.get_dom()[1]

    def is_in_img(self, y: float):
        return self.get_img()[0] <= y <= self.get_img()[1]

def intersection(s1 : Segment, s2: Segment):
    # m1 x + p1 = m2 x + p2
    # x = (p2 - p1) / (m1 - m2)
    if s1.get_m() == s2.get_m():
        if s1.get_p() == s2.get_p():
            all_ends = [s1.start, s1.end, s2.start, s2.end]
            all_ends.sort(key=lambda p: p.x)
            if all_ends[1].x == all_ends[2].x:
                return Point(all_ends[1].x, all_ends[1].y)
            raise ValueError("s1 and s2 are in the same line but not a single intersection point")
        raise ValueError("s1 and s2 are parallel. Can be no or infinity of points")
    x_intersect = (s2.get_p() - s1.get_p()) / (s1.get_m() - s2.get_m())
    if not (s1.is_in_dom(x_intersect) and s2.is_in_dom(x_intersect)):
        raise ValueError(f"Intersection point is not in DOM : {x_intersect}")
    y_intersect = s1.get_m() * x_intersect + s1.get_p()
    if not (s1.is_in_img(y_intersect) and s2.is_in_img(y_intersect)):
        raise ValueError(f"Intersection point is not in ING : {y_intersect}")
    return Point(x_intersect, y_intersect)


s1 = Segment(Point(0,0), Point(5,5))
s2 = Segment(Point(0,5), Point(5,0))
print(intersection(s1,s2))
s1 = Segment(Point(0,0), Point(1,1))
s2 = Segment(Point(1,1), Point(2,2))
print(intersection(s1,s2))
s1 = Segment(Point(0,0), Point(2,2))
s2 = Segment(Point(0,5), Point(2,3))
# print(intersection(s1,s2)) # Dom Error
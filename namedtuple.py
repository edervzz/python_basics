"""_summary_
    """
from collections import namedtuple

# similar a Records de C#
Point = namedtuple("Point", ["x", "y"])

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1.x)
print(p1.y)
print(p1 == p2)
